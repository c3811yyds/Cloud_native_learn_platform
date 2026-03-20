# -*- coding:utf-8 -*-
from flask import Blueprint, jsonify, request

from extensions import db
from models import PracticeStudent

practice_student_bp = Blueprint(
    "practice_students", __name__, url_prefix="/api/practice/students"
)


def ok(data=None, message="ok", code=0, status=200):
    return jsonify({"code": code, "message": message, "data": data}), status


def err(message="error", code=1, status=400, data=None):
    return jsonify({"code": code, "message": message, "data": data}), status


def as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def serialize_student(student: PracticeStudent):
    return {
        "id": student.id,
        "name": student.name,
        "major": student.major,
        "score": student.score,
        "created_at": student.created_at.isoformat() if student.created_at else None,
        "updated_at": student.updated_at.isoformat() if student.updated_at else None,
    }


def parse_student_payload(body, partial=False):
    data = {}

    if not partial or "name" in body:
        name = (body.get("name") or "").strip()
        if not name:
            return None, "name 不能为空"
        data["name"] = name

    if not partial or "major" in body:
        major = (body.get("major") or "").strip()
        if not major:
            return None, "major 不能为空"
        data["major"] = major

    if not partial or "score" in body:
        raw_score = body.get("score", 0)
        score = as_int(raw_score)
        if score is None:
            return None, "score 必须是整数"
        if score < 0 or score > 100:
            return None, "score 必须在 0 到 100 之间"
        data["score"] = score

    return data, None


@practice_student_bp.get("")
def list_students():
    keyword = (request.args.get("keyword") or "").strip()
    major = (request.args.get("major") or "").strip()

    query = PracticeStudent.query
    if keyword:
        query = query.filter(PracticeStudent.name.like(f"%{keyword}%"))
    if major:
        query = query.filter_by(major=major)

    students = query.order_by(PracticeStudent.id.asc()).all()
    return ok([serialize_student(student) for student in students])


@practice_student_bp.get("/<int:student_id>")
def get_student(student_id):
    student = PracticeStudent.query.get(student_id)
    if not student:
        return err("学生不存在", status=404)
    return ok(serialize_student(student))


@practice_student_bp.post("")
def create_student():
    body = request.get_json(silent=True) or {}
    payload, error = parse_student_payload(body)
    if error:
        return err(error)

    student = PracticeStudent(**payload)
    db.session.add(student)
    db.session.commit()
    return ok(serialize_student(student), "创建成功", status=201)


@practice_student_bp.put("/<int:student_id>")
def update_student(student_id):
    student = PracticeStudent.query.get(student_id)
    if not student:
        return err("学生不存在", status=404)

    body = request.get_json(silent=True) or {}
    payload, error = parse_student_payload(body, partial=True)
    if error:
        return err(error)
    if not payload:
        return err("至少传一个可更新字段: name、major、score")

    for key, value in payload.items():
        setattr(student, key, value)

    db.session.commit()
    return ok(serialize_student(student), "更新成功")


@practice_student_bp.delete("/<int:student_id>")
def delete_student(student_id):
    student = PracticeStudent.query.get(student_id)
    if not student:
        return err("学生不存在", status=404)

    db.session.delete(student)
    db.session.commit()
    return ok({"id": student_id}, "删除成功")
