from flask import render_template, flash, request
from app.forms import GenerateForm
from generate_text import generate
from app.main import bp

@bp.route('/', methods=['GET', 'POST'])
def index():
  try:
    form = GenerateForm()
    paragraphs = []
    
    if request.method=='POST' and form.validate_on_submit():
      number = form.number.data
      size = form.size.data
      flash(number)
      flash(size)
      paragraphs = generate(number, size)
  
    return render_template('index.html', title='PlantIpsum', form=form, paragraphs=paragraphs)
  except Exception as e:
    traceback.print_exc()
    return str(e)
