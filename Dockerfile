FROM python:3.11-alpine

WORKDIR /PyroEdgeGptBot

COPY . /PyroEdgeGptBot

ENV API_ID="17071638" \
    API_KEY="ce2045280ff29d36ff9a4daf1c84c975" \
    BOT_TOKEN="6053121132:AAGTOeZx3rV_qC5Eed9WUe-WjPJPgkk5QKs" \
    ALLOWED_USER_IDS="*" \
    SUPER_USER_IDS=51242184,449942659\
    NOT_ALLOW_INFO="⚠️You(%user_id%) are not authorized to use this bot⚠️" \
    BOT_NAME="AdvChatGpt" \
    SUGGEST_MODE=replykeyboard \
    DEFAULT_CONVERSATION_STYLE_TYPE=creative \
    RESPONSE_TYPE=normal \
    STREAM_INTERVAL=2 \
    LOG_LEVEL=WARNING \
    LOG_TIMEZONE=Asia/Shanghai


RUN apk update \
    &&  apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev git \
    &&  apk add libffi-dev \
    &&  apk add --no-cache curl-dev \
    &&  apk add --no-cache curl \
    &&  apk add --no-cache libcurl \
    &&  apk add --no-cache libressl \
    && pip install --no-cache-dir -r requirements.txt \ 
    && apk del .build-deps

CMD [ "python", "PyroEdgeGptBot.py" ]
