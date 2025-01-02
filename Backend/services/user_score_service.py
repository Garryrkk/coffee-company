from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from app.extensions import db

class UseScoreService:
    @staticmethod
    def calculate_loyalty_points(order):
        # Calculate loyalty points based on order total
        loyalty_points = int(order.total/10):
            return loyalty_points
    
    @staticmethod
    def update_user_score(user_id, order):
        user_score = UserScore(user_id=user_id)
        db.session.add(user_score)
        
    user_score.total_orders +=1
    user_score.total_spent += order.total_amount
    user_score.loyalty_points = UseScoreService.calculate_loyalty_points(order)
    
    # determine rank
    if user_score.loyalty_points >= 100:
        user_score.rank = "Gold"
    elif user_score.loyalty_points >= 50:
        user_score.rank = "Silver"
    else:
        user_score.rank = "Bronze"
        
        db.session.commit()
        return user_score
   
    
    