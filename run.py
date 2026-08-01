import os
import sys

from app import create_app
from app.config import Config
from ml_models.train_model import train_and_save_models
from scripts.seed_demo_data import seed_data

def main():
    print("=========================================================")
    print("  AI Network Intrusion Detection System (NIDS) v1.0")
    print("=========================================================")
    
    # 1. Verify ML Models
    scaler_path = os.path.join(Config.ML_MODEL_DIR, 'feature_scaler.pkl')
    rf_path = os.path.join(Config.ML_MODEL_DIR, 'rf_classifier.pkl')
    if not os.path.exists(rf_path) or not os.path.exists(scaler_path):
        print("[*] ML models missing. Training models...")
        train_and_save_models()
        
    # 2. Seed Database
    seed_data()
    
    # 3. Start Flask Web Dashboard Server
    app = create_app()
    print("\n[+] Dashboard URL: http://127.0.0.1:5000")
    print("[*] Press Ctrl+C to stop server.\n")
    
    # Run WSGI server
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    main()
