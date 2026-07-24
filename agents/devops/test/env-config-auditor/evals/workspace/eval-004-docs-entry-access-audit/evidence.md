# Runtime entry evidence

Staging Public has DNS, TLS, Service, Ingress, and a passing readiness probe. Production Public has a domain documented but the certificate and probe results cannot be inspected. Staging Internal is network-restricted and authenticated. Production Internal has a Service but no authentication policy evidence. Ports and values differ between staging and production.
