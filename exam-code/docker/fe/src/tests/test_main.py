"""
This module contains the Flask application for the frontend service.
"""

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Backend API URL
BACKEND_API_URL = (
    "http://backend-service:5001/fetch_price"
)
