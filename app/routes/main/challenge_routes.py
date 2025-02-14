from flask import request, jsonify
from flask_restful import Resource
from flask_restful_swagger import swagger
from app import db
from app.models.challenge import Challenge
from swagger_doc import (
    create_challenge_doc, get_challenges_doc, get_challenge_doc, 
    update_challenge_doc, delete_challenge_doc
)

class CreateChallengeResource(Resource):
    @swagger.operation(**create_challenge_doc)
    def post(self):
        data = request.get_json()
        new_challenge = Challenge(
            title=data.get('title'),
            description=data.get('description'),
            reward_points=data.get('reward_points'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date')
        )
        db.session.add(new_challenge)
        db.session.commit()
        return jsonify({'message': 'Challenge créé avec succès'}), 201

class GetChallengesResource(Resource):
    @swagger.operation(**get_challenges_doc)
    def get(self):
        challenges = Challenge.query.all()
        return jsonify([{
            'id': c.id,
            'title': c.title,
            'description': c.description,
            'reward_points': c.reward_points,
            'start_date': c.start_date,
            'end_date': c.end_date
        } for c in challenges]), 200

class GetChallengeResource(Resource):
    @swagger.operation(**get_challenge_doc)
    def get(self, challenge_id):
        challenge = Challenge.query.get_or_404(challenge_id)
        return jsonify({
            'id': challenge.id,
            'title': challenge.title,
            'description': challenge.description,
            'reward_points': challenge.reward_points,
            'start_date': challenge.start_date,
            'end_date': challenge.end_date
        }), 200

class UpdateChallengeResource(Resource):
    @swagger.operation(**update_challenge_doc)
    def put(self, challenge_id):
        challenge = Challenge.query.get_or_404(challenge_id)
        data = request.get_json()
        challenge.title = data.get('title', challenge.title)
        challenge.description = data.get('description', challenge.description)
        challenge.reward_points = data.get('reward_points', challenge.reward_points)
        challenge.start_date = data.get('start_date', challenge.start_date)
        challenge.end_date = data.get('end_date', challenge.end_date)
        db.session.commit()
        return jsonify({'message': 'Challenge mis à jour avec succès'}), 200

class DeleteChallengeResource(Resource):
    @swagger.operation(**delete_challenge_doc)
    def delete(self, challenge_id):
        challenge = Challenge.query.get_or_404(challenge_id)
        db.session.delete(challenge)
        db.session.commit()
        return jsonify({'message': 'Challenge supprimé avec succès'}), 200
