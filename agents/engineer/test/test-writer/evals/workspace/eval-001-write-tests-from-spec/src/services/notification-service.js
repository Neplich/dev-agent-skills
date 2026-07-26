export class NotificationService {
  constructor(repository) {
    this.repository = repository;
  }

  async create(input) {
    if (!input.recipientId) {
      throw new Error("recipientId is required");
    }
    if (!input.message?.trim()) {
      throw new Error("message is required");
    }
    return this.repository.create(input);
  }
}
