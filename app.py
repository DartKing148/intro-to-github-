from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, inputs, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
import datetime
import sys

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'
resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.DateTime('iso8601')
}


class Events(db.Model):
    __tablename__ = 'table_name'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


class EventGetResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Events.query.filter(Events.date == datetime.date.today()).all()


class PostEventResource(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument(
            'date',
            type=inputs.date,
            help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
            required=True
        )
        parser.add_argument(
            'event',
            type=str,
            help="The event name is required!",
            required=True
        )
        args = parser.parse_args()
        add_event = Events(event=str(args["event"]), date=args['date'])
        db.session.add(add_event)
        db.session.commit()
        event_name = args['event']
        date_name = args['date']
        return {"message": "The event has been added!",
                "event": event_name,
                "date": str(date_name.date())}

    @marshal_with(resource_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'start_time',
            type=inputs.date,
            help="The event date with the correct format is required! The correct format is YYYY-MM-DD!"
        )
        parser.add_argument(
            'end_time',
            type=inputs.date,
            help="The event date with the correct format is required! The correct format is YYYY-MM-DD!"
        )
        args = parser.parse_args()
        if args['start_time'] is None or args["end_time"] is None:
            event = Events.query.all()
            return event
        event = Events.query.filter(Events.date >= args["start_time"]).filter(args["end_time"] >= Events.date).all()
        return event


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        event = Events.query.filter(Events.id == event_id).first()
        if event is None:
            return abort(404, "The event doesn't exist!")
        return event

    @staticmethod
    def delete(event_id):
        event = Events.query.filter(Events.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        return {"message": "The event has been deleted!"}


db.create_all()

api = Api(app)
api.add_resource(EventGetResource, "/event/today")
api.add_resource(EventByID, '/event/<int:event_id>')
api.add_resource(PostEventResource, '/event')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
