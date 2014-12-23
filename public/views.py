from flask import Flask, request, abort, Response, redirect, url_for, flash, Blueprint
from flask.templating import render_template
from flask_security.decorators import roles_required, login_required
from public.models import Comic

bp_public = Blueprint('public',__name__, static_folder='../static')

@bp_public.route('/',defaults={'comic':None})
@bp_public.route('/<comic>')
def index(comic):
    if comic is None:
        comic=Comic.objects.order_by('-id').limit(1).first()
        next_comic = None
        prev_comic = Comic.objects.filter(id__lt=comic.id).order_by('-id').limit(1).first()
    else:
        try:
            comic = Comic.objects.get(id=comic)
            next_comic = Comic.objects.filter(id__gt=comic.id).order_by('-id').limit(1).first()
            prev_comic = Comic.objects.filter(id__lt=comic.id).order_by('-id').limit(1).first()
        except Exception, e:
            abort(404)
    return render_template('index.html',comic=comic, next_comic=next_comic, prev_comic=prev_comic)


@bp_public.route('/img/<id>')
def img(id):
    comic = Comic.objects(id=id).first()
    mime_type = comic.image.content_type
    return Response(comic.image.read(),mimetype=mime_type,direct_passthrough=True)



