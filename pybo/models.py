from pybo import db
#모든 모델의 기본 클래스인 db.Model을 상속받음.
#db는 init.py에서 생성한 SQLAlchemy 객체이다.


class Question(db.Model):
    #해당 모델을 통해서 테이블이 생성되면, 테이블 명은 question이 되고, 그 테이블을 Answer모델의 question.id와 연결 된다.
    #맨처음 파라미터는 데이터 타입
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(
        db.Integer, db.ForeignKey('question.id',
                                  ondelete='CASCADE'))  #해당 답변이 달리는 질문의 id
    #question_id의 목적 답변 모델에서 질문 모델을 참조하기 위해서
    # 답변 모델 데이터는 한 질문에 대한 답변으로 이루어지므로, 질문 모델과 연결된 속성이 필요함. 그것이 question_id속성이 되는것
    # 어떤 속성을 기존 모델과 연결지으려면 db.ForeinKey를 사용한다.
    # 즉 db.ForeinKey를 사용함으로서 기존 모델과 연결된다.
    # ondelete를 통해 질문이 삭제되면 해당 답변도 삭제되도록 한다.
    question = db.relationship(
        'Question', backref=db.backref('answer_set')
    )  #이 question모델은 기존의 question_id가 질문 모델과 답변 모델이 '연결'되도록 하는 것이었다면, 이것은 답변 모델이 질문 모델을 '참조'할 수 있도록 하기 위해서 만들어졌다.
    # 연결하는 것이기 때문에, 속성을 추가할 때, relationship을 이용함
    # db.relationship('참조할 모델명',backref=역참조 설정) 역참조 설정은 한개가 아닌 여러개를 참조해야 하므로, set을 활용함
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
