# API Documentation Schema

> Shared schema referenced by `api-gen` and `api-validator`.

## Required Sections

### 1. Document Metadata

```yaml
title: <Service Name> — API Documentation
version: <SemVer>
base_url: <https://api.example.com/v1>
auth_method: Bearer Token | API Key | OAuth 2.0 | None
date: <YYYY-MM-DD>
```

### 2. Overview

- Service purpose (1-2 sentences)
- Base URL and environments
- API versioning strategy
- **Quality**: Must include base URL and versioning approach.

### 3. Authentication

- Auth method description
- How to obtain credentials
- Example auth header
- **Quality**: Must include a concrete header example.

### 4. Common Headers

| Header | Required | Description | Example |
|--------|----------|-------------|---------|
| Authorization | Yes | Auth token | `Bearer <token>` |
| Content-Type | Yes | Request format | `application/json` |
| X-Request-Id | No | Tracing ID | `uuid-v4` |

### 5. Endpoints

For each endpoint:

#### `METHOD /path`

- **Summary**: One-line description
- **Auth**: Required / Optional / None
- **Rate Limit**: X requests/minute

**Path Parameters**

| Param | Type | Required | Description |
|-------|------|----------|-------------|

**Query Parameters**

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|

**Request Body**

```json
{
  "field": "type — description"
}
```

**Response** `200 OK`

```json
{
  "field": "type — description"
}
```

**Error Responses**

| Status | Code | Message | Description |
|--------|------|---------|-------------|

- **Quality**: Each endpoint must have method, path, at least one response, and error codes.

### 6. Data Models

For each model:

#### `ModelName`

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|

- **Quality**: All models referenced in endpoints must be defined.

### 7. Error Code Reference

| HTTP Status | Error Code | Description | Resolution |
|-------------|-----------|-------------|------------|
| 400 | INVALID_INPUT | Validation failed | Check request body |
| 401 | UNAUTHORIZED | Missing/invalid auth | Provide valid token |
| 404 | NOT_FOUND | Resource not found | Verify resource ID |
| 429 | RATE_LIMITED | Too many requests | Retry after delay |
| 500 | INTERNAL_ERROR | Server error | Contact support |

### 8. Pagination (if applicable)

- Pagination strategy (cursor / offset)
- Request parameters
- Response envelope format

### 9. Rate Limiting

- Limits per tier/endpoint
- Rate limit headers
- Retry strategy

### 10. Examples

- At least 1 complete request/response cycle using `curl` or equivalent
- **Quality**: Must be a working example with realistic data.

### 11. Changelog (Optional)

| Version | Date | Changes |
|---------|------|---------|

## Section Completeness Weights

| Section | Weight |
|---------|--------|
| Overview | 10% |
| Authentication | 10% |
| Endpoints | 35% |
| Data Models | 15% |
| Error Codes | 10% |
| Examples | 10% |
| Pagination / Rate Limiting | 10% |
