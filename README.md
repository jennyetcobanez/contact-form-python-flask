## 📡 REST API: Message Management

This project has been enhanced with a REST API that allows full CRUD (Create, Read, Update, Delete) for contact form submissions.

### Endpoints

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| GET    | /api/messages      | List all messages       |
| GET    | /api/messages/<id> | Get one message         |
| POST   | /api/messages      | Create new message      |
| PUT    | /api/messages/<id> | Update message          |
| DELETE | /api/messages/<id> | Delete message          |

### Sample POST Body
```json
{
  "name": "Jenny",
  "email": "jenny@example.com",
  "message": "This is a test message."
}
