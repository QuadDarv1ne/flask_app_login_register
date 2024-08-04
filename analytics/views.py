from flask import Blueprint, request
from app import db
from analytics.models import PageView

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/track', methods=['POST'])
def track():
    path = request.json.get('path')
    if path:
        page_view = PageView(path=path)
        db.session.add(page_view)
        db.session.commit()
        return '', 204
    return 'Invalid data', 400
