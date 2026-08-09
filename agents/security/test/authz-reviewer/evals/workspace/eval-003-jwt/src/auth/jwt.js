function decodeSegment(segment) {
  return JSON.parse(Buffer.from(segment, "base64url").toString("utf8"));
}

export function authenticateJwt(authorizationHeader) {
  const token = authorizationHeader.replace("Bearer ", "");
  const [, payload] = token.split(".");

  return decodeSegment(payload);
}

export function canAccessAdminApi(claims) {
  return claims.role === "admin";
}
