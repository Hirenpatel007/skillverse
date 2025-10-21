from django.conf import settings
import openai

class AIRecommender:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
    
    def get_career_recommendations(self, skills, career_goal, experience_level):
        """Get AI-powered career and learning recommendations"""
        prompt = f"""
        User Profile:
        - Skills: {skills}
        - Career Goal: {career_goal}
        - Experience Level: {experience_level}
        
        Provide 5 specific course recommendations and career advice in JSON format:
        {{
            "courses": ["course1", "course2", ...],
            "career_advice": "advice text",
            "skills_to_learn": ["skill1", "skill2", ...]
        }}
        """
        
        # Placeholder response (replace with actual OpenAI API call)
        return {
            "courses": ["Python for Data Science", "Machine Learning Basics", "Web Development"],
            "career_advice": "Focus on building projects and contributing to open source",
            "skills_to_learn": ["Python", "SQL", "Git"]
        }
    
    def generate_learning_path(self, user_profile):
        """Generate personalized learning path"""
        return {
            "title": "Personalized Learning Path",
            "description": "AI-generated path based on your goals",
            "courses": []
        }
