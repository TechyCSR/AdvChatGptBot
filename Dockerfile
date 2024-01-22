FROM python:3.11-alpine

WORKDIR /AdvChatGptBot

COPY . /AdvChatGptBot

ENV API_ID="" \
    API_KEY="" \
    BOT_TOKEN="" \
    ALLOWED_USER_IDS="*" \
    SUPER_USER_IDS=51242184\
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

CMD [ "python", "AdvChatGptBot.py" ]
