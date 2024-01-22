<div align="center">

# PyroEdgeGPTBot
_A telegram bot with Bing AI ( using [EdgeGPT](https://github.com/acheong08/EdgeGPT) API )_

<a>English</a> -
<a href="./README_zh.md">中文</a>

</div>

# Features
- [x] Multiple users with different sessions (No group support now)
- [x] Response with reference (and correct ref label)
- [x] Response with normal and stream mode
- [x] Can allow every one to use
- [x] Allow you set your own cookie at runtime
- [x] Allow you set a bot name to you
- [ ] Prompt Support
- [x] Image generation (inline query and command mode)
- [ ] Export conversation to Notion
- [x] Hot update the EdgeGPT dependence

# Setup
## Requirements
* python 3.8+
* A Microsoft Account with early access to [http://bing.com/chat](http://bing.com/chat)
* Telegram API_ID and API_KEY from [https://my.telegram.org/apps](https://my.telegram.org/apps)
* Telegram BOT_TOKEN from [@botfather](https://t.me/botfather)
* Good practical skills and a clear mind!

<details>
  <summary>

### Checking bing AI access (Required)
PS: Everyone can access Bing AI for chat now, even anonymous users.

  </summary>

- Install the latest version of Microsoft Edge
- Alternatively, you can use any browser and set the user-agent to look like you're using Edge. You can do this easily with an extension like "User-Agent Switcher and Manager" for [Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/).
- Open [bing.com/chat](https://bing.com/chat)
- If you see a chat feature, you are good to go

</details>


<details>
  <summary>

### Getting authentication (Optional)
PS: This column is needed by image creator, or ask more questions and have longer conversations

  </summary>

- Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/) or [Edge](https://microsoftedge.microsoft.com/addons/detail/cookieeditor/neaplmfkghagebokkhpjpoebhdledlfi)
- Go to [`bing.com`](https://bing.com/)
- Open the extension
- Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
- Paste your cookies into a file `./cookie.json` (The filename depends on your `.env` settings)

</details>

## Install requirements
```shell
pip install -r requirements.txt
```

## Set environment variables
```shell
cp .env.example .env
```
Then edit `.env` file and set `API_ID`, `API_KEY`, `BOT_TOKEN` and `ALLOWED_USER_IDS`. Or you can set environment variables like this:
```shell
export API_ID='1234567'
export API_KEY='abcdefg2hijk5lmnopq8rstuvwxyz9'
export BOT_TOKEN='123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
export ALLOWED_USER_IDS='112113115,567568569'
```

# Run
```shell
python PyroEdgeGptBot.py
```

# Run it on Back4app
* [Fork](https://github.com/tom-snow/PyroEdgeGPTBot/fork) this repo
* Login into [Back4app](https://www.back4app.com/login) (Suggests login with github account)
* Click `Build new app` and `Containers as a Service`
* Link the repo you forked.
* Set the [Required ENVS](./Dockerfile#L7-L11) (Explain [here](./.env.example#L4-L12))
> Note that you can run `python base64_encode_cookie.py` locally then get `COOKIE_BASE64` value from `base64_encoded_cookie.txt`
* Deploy!

# Run it on Railway (Recommend)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/7OO3yS?referralCode=_cP9IT)

<details>
  <summary>

## (Optional) Set bot commands

  </summary>

- Contact [@botfather](https://t.me/botfather)
- Send `/mybots` then select your bot and click `Edit Bot` -> `Edit Commands`
- Paste below and send.
```
start - Start the bot!
help - Get help
reset - Reset the bot
new - Create new conversation
switch - Switch the conversation style
interval - Set edit interval
suggest_mode - Set the suggest mode
image_gen - Generate images
update - Update the EdgeGPT dependence
cookie - Set you own cookie
bot_name - Set the bot name display to you
```

</details>

