export function ProfileSettingsForm() {
  return (
    <form aria-label="Profile settings">
      <label>
        Display name
        <input name="displayName" required maxLength={80} />
      </label>
      <label>
        Avatar URL
        <input name="avatarUrl" type="url" />
      </label>
      <label>
        Notification email
        <input name="notificationEmail" type="email" required />
      </label>
      <button type="submit">Save profile</button>
    </form>
  );
}
