# import os
# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# db = SQLAlchemy(app)

# # User Model
# linkedin_client_id = os.getenv('LINKEDIN_CLIENT_ID')
# linkedin_client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')
# linkedin_redirect_uri = os.getenv('LINKEDIN_REDIRECT_URI')


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     photo = db.Column(db.String(200), nullable=True)
# # Initialize database
# with app.app_context():
#     db.create_all()

# # Add student route
# @app.route('/students', methods=['POST'])
# def add_student():
#     data = request.json
#     name = data.get('name')
#     roll_no = data.get('roll_no')
#     year = data.get('year')
#     department = data.get('department')

#     if not name or not roll_no or not year or not department:
#         return jsonify({'success': False, 'message': 'Please fill all fields'})

#     new_student = User(name=name, roll_no=roll_no, year=year, department=department)
#     db.session.add(new_student)
#     db.session.commit()

#     return jsonify({'success': True, 'message': 'User added successfully'})

# # Get all students route
# def create_tables():
#     with app.app_context():
#         db.create_all()

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# @app.route('/user/signup', methods=['POST'])
# def signup():
#     data = request.form
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')
#     file = request.files.get('photo')

#     if not username or not email or not password:
#         return jsonify({'success': False, 'message': 'Please fill in all fields'})

#     existing_user = User.query.filter_by(email=email).first()
#     if existing_user:
#         return jsonify({'success': False, 'message': 'User already exists'})

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)
#     else:
#         filename = None

#     hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#     new_user = User(username=username, email=email, password=hashed_password, photo=filename)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({'success': True, 'message': 'User registered successfully'})
# # Load the text classification pipeline


# class PostLinkedIn:
#     def init(self):
#         self.access_token = None

#     def set_access_token(self, access_token):
#         self.access_token = access_token

#     def create_post(self, content):
#         if not self.access_token:
#             raise ValueError("Access token is not set.")
#         with open('linkedin_token.json', 'r') as f:
#             l_tokens = json.load(f)
#         url = 'https://api.linkedin.com/v2/ugcPosts'
#         headers = {
#             'Authorization': f'Bearer {self.access_token}',
#             'Content-Type': 'application/json'
#         }
#         payload = {
#             "author": f"urn:li:person:{l_tokens['id']}",
#             "lifecycleState": "PUBLISHED",
#             "specificContent": {
#                 "com.linkedin.ugc.ShareContent": {
                    
#                         "shareCommentary": {
#                             "text": content
#                         },
#                         "shareMediaCategory": "NONE"
                    
                    
#                 }
#             },
#             "visibility": {
#                 "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
#             }
#         }
#         response = requests.post(url, headers=headers, json=payload)
#         print("text response",response)
#         if response.status_code != 201:
#             print(f"Failed to create post: {response.json()}")
#         return response.json()

#     def create_post_with_image(self, content, image_urn):
#         if not self.access_token:
#             raise ValueError("Access token is not set.")
#         with open('linkedin_token.json', 'r') as f:
#             l_tokens = json.load(f)
        

#         url = 'https://api.linkedin.com/v2/ugcPosts'
#         headers = {
#             'Authorization': f'Bearer {self.access_token}',
#             'Content-Type': 'application/json'
#         }
#         payload = {
#             "author": f"urn:li:person:{l_tokens['id']}",
#             "lifecycleState": "PUBLISHED",
#             "specificContent": {
#                 "com.linkedin.ugc.ShareContent": {
                   
#                         "shareCommentary": {
#                             "text": content
#                         },
#                         "shareMediaCategory": "IMAGE",
#                         "media": [
#                             {
#                                 "status": "READY",
#                                 "description": {
#                                     "text": "Image description"
#                                 },
#                                 "media": image_urn,
#                                 "title": {
#                                     "text": "Image Title"
#                                 }
#                             }
#                         ]
                    
#                 }
#             },
#             "visibility": {
#                 "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
#             }
#         }
#         response = requests.post(url, headers=headers, json=payload)
#         if response.status_code != 201:
#             print(f"Failed to create post with image: {response.json()}")
#         return response.json()


# class LinkedinManager:
#     def init(self):
#         self.access_token = None
#         self.user_id = None
#         self.load_tokens()

#     def load_tokens(self):
#         try:
#             with open("linkedin_token.json", 'r') as f:
#                 token = json.load(f)
#                 self.access_token = token.get("access_token")
#                 self.user_id = token.get("id")

#             if not self.access_token or not self.user_id:
#                 raise ValueError("LinkedIn token or ID is missing in linkedin_token.json")

#         except FileNotFoundError:
#             print("linkedin_token.json file not found.")
#         except ValueError as ve:
#             print(f"Error: {ve}")
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")

#     def upload_image_to_linkedin(self,access_token:str, user_id:str, image_path):
#         """Upload an image to LinkedIn and return the upload reference."""
#         # Initialize the upload
#         init_url = "https://api.linkedin.com/v2/assets?action=registerUpload"
#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json"
#         }
#         upload_request_body = {
#             "registerUploadRequest": {
#                 "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
#                 "owner": f"urn:li:person:{user_id}",
#                 "serviceRelationships": [
#                     {
#                         "relationshipType": "OWNER",
#                         "identifier": "urn:li:userGeneratedContent"
#                     }
#                 ]
#             }
#         }

#         response = requests.post(init_url, headers=headers, json=upload_request_body)
#         response.raise_for_status()

#         upload_info = response.json()
#         upload_url = upload_info['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
#         asset = upload_info['value']['asset']

#         # Upload the image
#         with open(image_path, 'rb') as image_file:
#             image_headers = {
#                 "Authorization": f"Bearer {access_token}",
#                 "Content-Type": "application/octet-stream"
#             }
#             image_response = requests.put(upload_url, headers=image_headers, data=image_file)
#             image_response.raise_for_status()

#             return asset

#     def post_to_linkedin(self, content, image_path=None):
#         # if not self.access_token:
#         #     raise ValueError("Access token is not available. Please log in to LinkedIn first.")
#         with open("linkedin_token.json", 'r') as f:
#                 token = json.load(f)
#                 self.access_token = token.get("access_token")
#                 self.user_id = token.get("id")
#         linkedin = PostLinkedIn()
#         linkedin.set_access_token(self.access_token)

#         if image_path:
#             image_urn = self.upload_image_to_linkedin(self.access_token,self.user_id,image_path)
#             response = linkedin.create_post_with_image(content, image_urn)
#         else:
#             response = linkedin.create_post(content)
#         return response

# # User model

# if __name__ == '__main__':
#         port = int(os.environ.get("PORT", 5000))
#         app.run(host='0.0.0.0', port=port)
import os
import json
import base64
import hashlib
import re
from flask import Flask, render_template, request, session, redirect, jsonify, send_from_directory
from requests_oauthlib import OAuth2Session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import requests
# import facebook
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
import httplib2
# from twitter.crew import Twitter
# from summarizer.ytsum import YouTubeTranscriptSummarizer
from LinkedIn.crew import CrewLinkedIn
from transformers import pipeline
# from fb.crew import Facebook
from langchain_community.agent_toolkits import GmailToolkit
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.load import dumps, loads
from langchain_core.messages import AIMessage, HumanMessage
# from youtube.crew import YouTubeTitleCreator, YouTubeDescriptCreator
import random
import time
# from zenora import APIClient
# from discord.creds import TOKEN, CLIENT_SECRET, REDIRECT_URI, OAUTH_URL

load_dotenv()
# pipe = pipeline("text-classification", model="Varun53/openai-roberta-large-AI-detection")
app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"] = os.urandom(24)
# fb = Facebook()

# Database and file upload configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)

# Ensure upload folder and output directories exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists('outputs/ytVideoSummarizer'):
    os.makedirs('outputs/ytVideoSummarizer')

# Twitter OAuth configuration
client_id = os.getenv("TWITTER_OAUTH_CLIENT_ID")
client_secret = os.getenv("TWITTER_OAUTH_CLIENT_SECRET")
redirect_uri = "http://127.0.0.1:5000/oauth/callback"
auth_url = "https://twitter.com/i/oauth2/authorize"
token_url = "https://api.twitter.com/2/oauth2/token"
scopes = ["tweet.read", "users.read", "tweet.write", "offline.access"]

linkedin_client_id = os.getenv('LINKEDIN_CLIENT_ID')
linkedin_client_secret = os.getenv('LINKEDIN_CLIENT_SECRET')
linkedin_redirect_uri = os.getenv('LINKEDIN_REDIRECT_URI')

class PostLinkedIn:
    def init(self):
        self.access_token = None

    def set_access_token(self, access_token):
        self.access_token = access_token

    def create_post(self, content):
        if not self.access_token:
            raise ValueError("Access token is not set.")
        with open('linkedin_token.json', 'r') as f:
            l_tokens = json.load(f)
        url = 'https://api.linkedin.com/v2/ugcPosts'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            "author": f"urn:li:person:{l_tokens['id']}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    
                        "shareCommentary": {
                            "text": content
                        },
                        "shareMediaCategory": "NONE"
                    
                    
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        print("text response",response)
        if response.status_code != 201:
            print(f"Failed to create post: {response.json()}")
        return response.json()

    def create_post_with_image(self, content, image_urn):
        if not self.access_token:
            raise ValueError("Access token is not set.")
        with open('linkedin_token.json', 'r') as f:
            l_tokens = json.load(f)
        

        url = 'https://api.linkedin.com/v2/ugcPosts'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        payload = {
            "author": f"urn:li:person:{l_tokens['id']}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                   
                        "shareCommentary": {
                            "text": content
                        },
                        "shareMediaCategory": "IMAGE",
                        "media": [
                            {
                                "status": "READY",
                                "description": {
                                    "text": "Image description"
                                },
                                "media": image_urn,
                                "title": {
                                    "text": "Image Title"
                                }
                            }
                        ]
                    
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 201:
            print(f"Failed to create post with image: {response.json()}")
        return response.json()


class LinkedinManager:
    def init(self):
        self.access_token = None
        self.user_id = None
        self.load_tokens()

    def load_tokens(self):
        try:
            with open("linkedin_token.json", 'r') as f:
                token = json.load(f)
                self.access_token = token.get("access_token")
                self.user_id = token.get("id")

            if not self.access_token or not self.user_id:
                raise ValueError("LinkedIn token or ID is missing in linkedin_token.json")

        except FileNotFoundError:
            print("linkedin_token.json file not found.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def upload_image_to_linkedin(self,access_token:str, user_id:str, image_path):
        """Upload an image to LinkedIn and return the upload reference."""
        # Initialize the upload
        init_url = "https://api.linkedin.com/v2/assets?action=registerUpload"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        upload_request_body = {
            "registerUploadRequest": {
                "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
                "owner": f"urn:li:person:{user_id}",
                "serviceRelationships": [
                    {
                        "relationshipType": "OWNER",
                        "identifier": "urn:li:userGeneratedContent"
                    }
                ]
            }
        }

        response = requests.post(init_url, headers=headers, json=upload_request_body)
        response.raise_for_status()

        upload_info = response.json()
        upload_url = upload_info['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
        asset = upload_info['value']['asset']

        # Upload the image
        with open(image_path, 'rb') as image_file:
            image_headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/octet-stream"
            }
            image_response = requests.put(upload_url, headers=image_headers, data=image_file)
            image_response.raise_for_status()

            return asset

    def post_to_linkedin(self, content, image_path=None):
        # if not self.access_token:
        #     raise ValueError("Access token is not available. Please log in to LinkedIn first.")
        with open("linkedin_token.json", 'r') as f:
                token = json.load(f)
                self.access_token = token.get("access_token")
                self.user_id = token.get("id")
        linkedin = PostLinkedIn()
        linkedin.set_access_token(self.access_token)

        if image_path:
            image_urn = self.upload_image_to_linkedin(self.access_token,self.user_id,image_path)
            response = linkedin.create_post_with_image(content, image_urn)
        else:
            response = linkedin.create_post(content)
        return response

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    photo = db.Column(db.String(200), nullable=True)

# Facebook Manager
def create_tables():
    with app.app_context():
        db.create_all()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/user/signup', methods=['POST'])
def signup():
    data = request.form
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    file = request.files.get('photo')

    if not username or not email or not password:
        return jsonify({'success': False, 'message': 'Please fill in all fields'})

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'success': False, 'message': 'User already exists'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
    else:
        filename = None

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, email=email, password=hashed_password, photo=filename)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'User registered successfully'})
# Load the text classification pipeline

@app.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Please fill in all fields'})

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'success': False, 'message': 'User does not exist'})

    if not check_password_hash(user.password, password):
        return jsonify({'success': False, 'message': 'Incorrect password'})

    return jsonify({'success': True, 'message': 'Login successful', 'username': user.username, 'photo': user.photo})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/summary/<filename>', methods=['GET'])
def get_summary(filename):
    file_path = os.path.join('outputs/ytVideoSummarizer', filename)
    if not os.path.isfile(file_path):
        return jsonify({'success': False, 'message': 'File not found'}), 404

    return send_from_directory('outputs/ytVideoSummarizer', filename)
@app.route('/outputs/<path:filename>')
def serve_output(filename):
    return send_from_directory('outputs', filename)
# Twitter OAuth functions
def create_code_verifier():
    code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
    return re.sub("[^a-zA-Z0-9]+", "", code_verifier)

def create_code_challenge(code_verifier):
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(code_challenge).decode("utf-8").replace("=", "")

code_verifier = create_code_verifier()
code_challenge = create_code_challenge(code_verifier)

@app.route('/linkedin/check_connected', methods=['GET'])
def linkedin_check_connected():
    if os.path.exists('linkedin_token.json'):
        return jsonify({'connected': True})
    return jsonify({'connected': False})
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path and os.path.exists("frontend/build/" + path):
        return send_from_directory("frontend/build", path)
    else:
        return send_from_directory("frontend/build", "index.html")


@app.route('/linkedin/login')
def linkedin_login():
    print("1")
    session.clear()
    authorization_url = 'https://www.linkedin.com/oauth/v2/authorization'
    params = {
        'response_type': 'code',
        'client_id': linkedin_client_id,
        'redirect_uri': linkedin_redirect_uri,
        'scope': 'openid+profile+email+w_member_social'
    }
    url = f"{authorization_url}?response_type={params['response_type']}&client_id={params['client_id']}&redirect_uri={params['redirect_uri']}&scope={params['scope']}"
    return redirect(url)

@app.route('/linkedin/callback')
def linkedin_callback():
    code = request.args.get('code')
    
    if code:
        user = session.get('user_id')
        access_token = get_linkedin_access_token(code)
        if access_token:
            session['linkedin_access_token'] = access_token
            uid = get_linkedin_id(access_token)
            with open("linkedin_token.json", "w") as f:
                json.dump({"access_token": access_token, "id": uid}, f)
            return 'Linkedin oauth very succesful'
            
        else:
            return 'Failed to get access token!'
    else:
        return 'LinkedIn OAuth failed!'
  
def get_linkedin_access_token(code):
    access_token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': linkedin_redirect_uri,
        'client_id': linkedin_client_id,
        'client_secret': linkedin_client_secret
    }
    response = requests.post(access_token_url, data=data)
    print(f"Response from LinkedIn access token request: {response.json()}")
    return response.json().get('access_token')

def get_linkedin_id(access_token):
    url = 'https://api.linkedin.com/v2/userinfo'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    return response.json().get('sub')
@app.route('/generate_linkedin_content', methods=['POST'])
def generate_linkedin_content():
    try:
        # Extract content from request
        content = request.form.get('content')
        image = request.files.get('image')

        if not content:
            return jsonify({'error': 'Content is required to generate a LinkedIn post'}), 400

        # Initialize LinkedIn content generation
        l_crew = CrewLinkedIn()
        generated_content = l_crew.run(content)  # Generate content using Crewai

        # Prepare image if provided
        image_path = None
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            # Construct the image URL (assuming a static file server setup)
            image_url = request.host_url + 'uploads/' + filename
        else:
            image_url = None

        # Return generated content and image URL
        return jsonify({'content': str(generated_content), 'image_url': image_url})

    except Exception as e:
        app.logger.error(f'Error in generate_linkedin_content route: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/post_linkedin', methods=['POST'])
def post_linkedin():
    try:
        content = request.form.get('content')
        image = request.files.get('image')

        if not content:
            return jsonify({'success': False, 'message': 'Content is required to post to LinkedIn.'})

        # Save the image if provided
        image_path = None
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)

        # Initialize LinkedIn manager and post content
        linkedin_manager = LinkedinManager()
        response = linkedin_manager.post_to_linkedin(content, image_path)

        # Handle response
        
        return jsonify({'success': True, 'message': 'Post published to LinkedIn', 'response': response})
        # else:
        #     return jsonify({'success': False, 'message': f'Failed to post content to LinkedIn: {response.text}'})
    except Exception as e:
        app.logger.error(f'Error in post_linkedin route: {str(e)}')
        return jsonify({'success': False, 'message': str(e)}), 500


if __name__ == '__main__':
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)