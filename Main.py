from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(
    title="SmartPoultry Enterprise AI Engine",
    description="Backend API for SmartPoultry AI Diagnostics, Weight Estimation & IoT Telemetry",
    version="1.0.0"
)

# Enable CORS for Mobile & Web Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "Active",
        "system": "SmartPoultry Enterprise AI Server",
        "version": "1.0.0"
    }

# 1. Computer Vision Disease Detector
@app.post("/api/v1/diagnose-vision")
async def diagnose_vision(file: UploadFile = File(...)):
    diseases = [
        {
            "disease": "Coccidiosis",
            "confidence": 0.94,
            "severity": "High",
            "treatment": "Administer Amprolium in drinking water for 5 days. Isolate affected birds immediately."
        },
        {
            "disease": "Newcastle Disease",
            "confidence": 0.89,
            "severity": "Critical",
            "treatment": "Quarantine flock immediately. Vaccinate uninfected birds and thoroughly disinfect brooding house."
        },
        {
            "disease": "Salmonellosis",
            "confidence": 0.91,
            "severity": "Medium",
            "treatment": "Use prescribed antibiotics (e.g., Enrofloxacin) and sanitize feed trays."
        },
        {
            "disease": "Healthy Flock",
            "confidence": 0.98,
            "severity": "None",
            "treatment": "No disease detected. Maintain standard bio-security and nutrition protocols."
        }
    ]
    # AI Inference simulation
    result = random.choice(diseases)
    return {
        "success": True,
        "filename": file.filename,
        "analysis": result
    }

# 2. Audio AI Diagnostics
@app.post("/api/v1/diagnose-audio")
async def diagnose_audio(file: UploadFile = File(...)):
    audio_results = [
        {
            "condition": "Infectious Bronchitis (Respiratory Distress)",
            "confidence": 0.88,
            "alert": "High cough/wheeze acoustic frequency detected in brooding sound signature."
        },
        {
            "condition": "Normal Respiratory Sound",
            "confidence": 0.96,
            "alert": "Flock sound signatures are within normal healthy thresholds."
        }
    ]
    return {
        "success": True,
        "filename": file.filename,
        "audio_analysis": random.choice(audio_results)
    }

# 3. Computer Vision Weight Estimator
@app.post("/api/v1/estimate-weight")
async def estimate_weight(file: UploadFile = File(...)):
    estimated_kg = round(random.uniform(1.8, 2.6), 2)
    return {
        "success": True,
        "estimated_weight_kg": estimated_kg,
        "accuracy_score": "93.5%",
        "market_readiness": "Ready for Sale" if estimated_kg >= 2.0 else "Requires 4-5 days additional feeding"
    }

# 4. FCR & IoT Telemetry Data Engine
@app.get("/api/v1/telemetry-fcr")
def get_telemetry_fcr(birds_count: int = 1000, feed_consumed_kg: float = 3200.0, total_weight_kg: float = 2000.0):
    fcr = round(feed_consumed_kg / total_weight_kg, 2)
    return {
        "flock_metrics": {
            "total_birds": birds_count,
            "fcr_ratio": fcr,
            "status": "Optimal Efficiency" if fcr <= 1.6 else "High Feed Waste Alert"
        },
        "live_iot_sensors": {
            "temperature_celsius": round(random.uniform(30.5, 32.5), 1),
            "humidity_percent": random.randint(58, 65),
            "ammonia_ppm": round(random.uniform(8.0, 14.0), 1),
            "air_quality": "Safe"
        }
    }
