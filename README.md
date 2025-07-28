# Math Operations API

## Descriere

Acest proiect este o aplicație web modulară construită cu Flask, care oferă operații matematice (putere, factorial, Fibonacci), autentificare cu JWT, logare evenimente în Kafka, caching cu Redis, metrici Prometheus și persistare date în MySQL. Include o interfață web modernă pentru utilizatori și API-uri pentru operații matematice.

## Tehnologii folosite
- Python 3.10+
- Flask
- MySQL
- Redis
- Kafka & Zookeeper
- Docker & Docker Compose
- Prometheus
- Pydantic (validare request-uri)
- Werkzeug (hashing parole)
- JWT (PyJWT)

## Structura proiectului
```
app/
  controller/         # Logica pentru autentificare, operații matematice, înregistrare
  model/              # Interacțiune cu baza de date (utilizatori, operații)
  routes/             # Rute Flask (API și pagini)
  schemas/            # Schemas Pydantic pentru validare request/response
  utils/              # Utilitare: JWT, Kafka, cache, etc
  view/               # HTML, JS, CSS pentru frontend
  logger.log          # Loguri tehnice
  kafka_consumed.log  # Loguri business/event din Kafka
requirements.txt      # Dependențe Python
Dockerfile            # Build imagine backend
```

## Funcționalități principale
- **Autentificare și înregistrare** cu JWT, validare AJAX, mesaje toast
- **Operații matematice**: putere, factorial, Fibonacci (API REST)
- **Persistență**: utilizatori și operații în MySQL
- **Caching**: rezultate operații cu Redis
- **Logare evenimente**: Kafka producer (la acțiuni cheie), consumer (scrie în fișier)
- **Metrici Prometheus**: endpoint `/metrics` pentru monitorizare
- **Streaming loguri**: endpoint pentru ultimele N linii din log Kafka
- **Frontend modern**: pagini HTML cu AJAX, feedback instant

## Cum rulezi proiectul (local cu Docker Compose)
1. Clonează repo-ul și intră în director:
   ```sh
   git clone <repo-url>
   cd Math-operations
   ```
2. Pornește toate serviciile:
   ```sh
   docker-compose up --build
   ```
3. Accesează aplicația la `http://localhost:5000/mathSolve/login`

## Endpoints principale
- `/mathSolve/login` și `/mathSolve/register` — autentificare și înregistrare
- `/mathSolve/power`, `/mathSolve/fibonacci`, `/mathSolve/factorial` — API POST pentru operații matematice
- `/metrics` — metrici Prometheus
- `/stream-logs` — streaming loguri Kafka

## Configurare variabile de mediu
- `SECRET_KEY` — cheie secretă JWT (default: `dev_secret`)
- Setează în `.env` sau direct în Docker Compose

## Note suplimentare
- Pentru dezvoltare locală fără Docker, instalează dependențele cu `pip install -r requirements.txt` și pornește serviciile necesare (MySQL, Redis, Kafka) manual.
- Codul respectă PEP8/flake8.

## Autori
- [Numele tău]
