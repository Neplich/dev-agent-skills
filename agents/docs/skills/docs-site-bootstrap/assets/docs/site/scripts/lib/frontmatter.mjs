import {
  DOC_TYPES, STAGES, VISIBILITIES, collectMarkdown
} from './pages.mjs';

const REQUIRED = [
  'title', 'visibility', 'doc_type', 'stage', 'owners', 'related_code',
  'last_verified_version'
];

const nonEmptyStrings = (value) => Array.isArray(value)
  && value.length > 0
  && value.every((item) => typeof item === 'string' && item.trim() !== '');

export function validatePage(page) {
  const data = page.data;
  const errors = [];
  for (const key of REQUIRED) {
    if (!(key in data) || data[key] === null || data[key] === '') {
      errors.push(`missing required field "${key}"`);
    }
  }
  if (typeof data.title !== 'string' || data.title.trim() === '') {
    errors.push('title must be a non-empty string');
  }
  if (!VISIBILITIES.has(data.visibility)) {
    errors.push('visibility must be public, internal, or both');
  }
  if (!DOC_TYPES.has(data.doc_type)) {
    errors.push('doc_type has an unsupported value');
  }
  if (!STAGES.has(data.stage)) {
    errors.push('stage must be draft, dev, ops, or release');
  }
  if (!nonEmptyStrings(data.owners)) {
    errors.push('owners must be a non-empty string array');
  }
  if (!nonEmptyStrings(data.related_code)) {
    errors.push('related_code must be a non-empty string array');
  }
  if (typeof data.last_verified_version !== 'string'
      || data.last_verified_version.trim() === '') {
    errors.push('last_verified_version must be a version anchor or unverified');
  }
  return errors;
}

export async function collectFrontmatterFailures() {
  const failures = [];
  for (const page of await collectMarkdown()) {
    const errors = validatePage(page);
    if (errors.length) failures.push({ path: page.relativePath, errors });
  }
  return failures;
}
