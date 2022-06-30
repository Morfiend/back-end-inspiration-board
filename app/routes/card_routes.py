from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.card import Card


cards_bp = Blueprint('cards', __name__, url_prefix="/cards")


#DELETE a card
@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_one_card(card_id):
    # validate card_id
    try:
        card_id = int(card_id)
    except:
        abort(make_response({"message": f"Card{card_id} is invalid"}, 400))
    # get card
    card = Card.query.get(card_id)
    # if task id not exist
    if not card:
        abort(make_response({"message": f"Card{card_id} not found"}, 404))

    db.session.delete(card)
    db.session.commit()
    return {"details": f'Card {card_id} successfully deleted'}
        

#UPDATE likes count for a card
@cards_bp.route("/<card_id>", methods=["PUT"])
def update_likes_for_one_card(card_id):
    # validate card_id
    try:
        card_id = int(card_id)
    except:
        abort(make_response({"message": f"Card{card_id} is invalid"}, 400))
    # get card
    card = Card.query.get(card_id)
    # if task id not exist
    if not card:
        abort(make_response({"message": f"Card{card_id} not found"}, 404))
    
    request_body = request.get_json()
    card.likes_count = request_body["likes_count"]

    db.session.commit()

    return {"card": card.to_json()}, 200