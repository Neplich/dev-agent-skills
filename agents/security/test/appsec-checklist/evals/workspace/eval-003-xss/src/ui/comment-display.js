export function renderComments(container, comments) {
  container.innerHTML = comments
    .map((comment) => `<article><h3>${comment.author}</h3><p>${comment.body}</p></article>`)
    .join("");
}
