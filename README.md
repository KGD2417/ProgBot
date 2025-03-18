# 🤖 Hugging Face API Chatbot

A chatbot built using **FastAPI** for the backend and **React.js** for the frontend, utilizing **Hugging Face API** for AI-based responses.

## 🚀 Features
- Uses **Hugging Face Transformers** API
- **FastAPI** backend with RESTful API
- **React.js** frontend with an interactive chat UI
- Easy to deploy and extend

---

## 📂 Project Structure
```
📁 ProgChatBot
├── 📂 backend (FastAPI backend)
│   ├── chatbot.py (FastAPI app using Hugging Face API)
│   ├── requirements.txt (Dependencies)
├── 📂 frontend (React.js frontend)
│   ├── src
│   │   ├── App.js (Main React component)
│   │   ├── Chat.js (Chat UI component)
│   │   ├── api.js (API calls to FastAPI backend)
│   ├── package.json
├── README.md
```

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/ProgChatBot.git
cd ProgChatBot
```

### 2️⃣ Setup Backend (FastAPI)
#### Install Dependencies
```sh
cd backend
pip install -r requirements.txt
```
#### Start the FastAPI Server
```sh
uvicorn chatbot:app --reload
```
Backend will run at: **http://127.0.0.1:8000**

---

### 3️⃣ Setup Frontend (React.js)
#### Install Dependencies
```sh
cd ../frontend
npm install
```
#### Start the React App
```sh
npm start
```
Frontend will run at: **http://localhost:3000**

---

## 🛠️ API Endpoints
| Method | Endpoint  | Description |
|--------|----------|-------------|
| POST   | `/chat`  | Send a message to the chatbot and receive a response |

---

## 🔧 Environment Variables
Create a **.env** file in the `backend` folder and add your **Hugging Face API key**:
```
HF_API_KEY=your_huggingface_api_key
```

---

## 🎯 Deployment
### Deploy Backend
```sh
uvicorn chatbot:app --host 0.0.0.0 --port 8000
```
### Deploy Frontend
Use **Vercel** or **Netlify** for easy deployment.
```sh
npm run build
```

---

## 👨‍💻 Contributing
Feel free to submit **issues** and **pull requests** to improve the chatbot! 🚀

---

## 📜 License
MIT License

