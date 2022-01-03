from flask import Blueprint, render_template
#render_template은 템플릿 화면을 화면으로 렌더링해주는 것 템플릿 파일을 통해서 화면을 구성할 수 있다.
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, pybo!'


@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    #질문 목록 데이터 얻기, 작성일시 기준 역순으로 나열하도록 함
    return render_template('/question/question_list.html',
                           question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)  #페이지가 없을시 404페이지를 띄운다.
    return render_template('question/question_detail.html', question=question)
