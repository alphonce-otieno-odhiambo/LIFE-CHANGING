from flask import render_template,request,redirect,url_for,abort
from .forms import UpdateProfile,PitchForm,CommentsForm
from .. import db,photos
from . import main
from ..models import User,Pitches,Comments,Upvote,Downvote
from flask_login import login_required,current_user
from ..search import get_pitches,get_pitch

# Views functions
@main.route('/',methods = ["GET","POST"])
def  index():
  '''
  Function that returns the home page
  '''
  form = PitchForm()
  if form.validate_on_submit():
    new_pitch = Pitches(pitch_category = form.pitch_category.data, pitch_title = form.pitch_title.data,pitch = form.pitch.data,user=current_user)
    new_pitch.save_pitch()
    
  title = "Impression in 60 seconds"
  return render_template('index.html',title = title,pitch_form = form)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/game')
def  gamepitch():
  '''
  Function that returns data displayed in the gamepitch template
  '''
  game_pitches = get_pitches("Game pitch")
  title = "Impression in 60 seconds-gamepitch"
  return render_template('pitch-categories/game.html',title = title, game_pitches = game_pitches)

@main.route('/interview')
def  interviewpitch():
  '''
  Function that returns the data of interview pitch 
  '''
  interview_pitches = get_pitches("Interview pitch")
  title = "Impression in 60 seconds-interviewpitch"
  return render_template('pitch-categories/interview.html',title = title,interview_pitches = interview_pitches )

@main.route('/pickuplines')
def  pickuplinespitch():
  '''
  Function that returns pickuplines contents
  '''
  pickuplines_pitches = get_pitches("Pick-up lines")
  title = "Impression in 60 seconds-pickuplinespitch"
  return render_template('pitch-categories/pickuplines.html',title = title, pickuplines_pitches = pickuplines_pitches)

@main.route('/project')
def  projectpitch():
  '''
  Function that returns the projectpitch page and its contents
  '''
  project_pitches = get_pitches("Project pitch")
  title = "Impression in 60 seconds-projectpitch"
  return render_template('pitch-categories/project.html',title = title, project_pitches = project_pitches)
@main.route('/comments/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id): 
  form = CommentsForm()
  pitch = get_pitch(id) 
  print(pitch)
  
  if form.validate_on_submit(): 
    
    # Updated comment instance
    new_comment = Comments(comment = form.comment.data,user=current_user,pitch_id = id)
    new_comment.save_comment()
  
  comments_found = Comments.get_comments(id)
  title = 'Comments'
  return render_template('new_comment.html', title = title, comments_form = form, pitch = pitch,comments_found = comments_found)

@main.route('/like/<int:id>', methods = ['POST', 'GET'])
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    for pitch in get_pitches:
      continue
    new_vote = Upvote( pitch_id=id)
    new_vote.save()     
    return redirect(url_for('main.index'))    

@main.route('/dislike/<int:id>', methods = ['POST','GET'])
def dislike(id):
    get_pitch = Downvote.get_downvotes(id)
    for pitch in get_pitch:
      continue
    new_downvote = Downvote(pitch_id=id)
    new_downvote.save()     
    return redirect(url_for('main.index'))  