"""
ClipFly Telegram Bot - Configuration File
Edit this file to add your bot token and other settings
"""

# ============================================================================
# TELEGRAM BOT TOKEN
# ============================================================================
# Replace with your actual bot token from @BotFather
BOT_TOKEN = "7738665424:AAEjJiduAjbvnqbwAEGrEWEd_oO1adptK5I"

# ============================================================================
# CLIPFLY API CONFIGURATION
# ============================================================================
BASE_URL = "https://www.clipfly.ai"
GENERATOR_ENDPOINT = "/api/v1/user/ai-tasks/image-generator/create"
QUEUE_ENDPOINT = "/api/v1/user/ai-tasks/ai-generator/queue-list"
TASK_DETAIL_ENDPOINT = "/api/v1/user/ai-tasks/image-generator/detail"

# ============================================================================
# FILE LOCATIONS
# ============================================================================
TOKEN_FILE = "token.txt"  # File containing ClipFly API tokens (one per line)
IMAGES_DIR = "generated_images"  # Directory to save generated images

# ============================================================================
# IMAGE GENERATION SETTINGS
# ============================================================================
MAX_WAIT_TIME = 300  # Maximum time to wait for generation (seconds)
CHECK_INTERVAL = 1  # How often to check status (seconds)

# ============================================================================
# AVAILABLE AI MODELS
# ============================================================================
AVAILABLE_MODELS = {
    "1": {"id": "nanobanana", "name": "🍌 Nanobanana (Basic)", "desc": "Fast, basic quality"},
    "2": {"id": "nanobanana2", "name": "🍌 Nanobanana Pro", "desc": "Enhanced quality"},
    "3": {"id": "Seedream4", "name": "🌱 Seedream 4", "desc": "Artistic style"},
    "4": {"id": "qwen", "name": "🤖 Qwen", "desc": "Balanced quality"},
    "5": {"id": "gpt_1low", "name": "⚡ GPT-1 Low", "desc": "Fast generation"},
    "6": {"id": "gpt_1medium", "name": "🎯 GPT-1 Medium", "desc": "Better quality"},
    "7": {"id": "flux_kontext_pro", "name": "✨ Flux Kontext Pro", "desc": "Premium quality"},
    "8": {"id": "flux_2_pro", "name": "🚀 Flux Kontext Pro 2", "desc": "Version 2 of Kontext Pro"},
    "9": {"id": "clipfly_2", "name": "🎬 Clipfly 2", "desc": "Clipfly version"},
    "10": {"id": "midjourney_v7", "name": "🎨 Midjourney V7", "desc": "Midjourney V7 - more detailed textures"}
}

DEFAULT_MODEL = "nanobanana"

# ============================================================================
# LOGGING SETTINGS
# ============================================================================
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL




