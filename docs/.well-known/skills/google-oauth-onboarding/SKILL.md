---
name: google-oauth-onboarding
description: Guide Google Cloud setup and OAuth consent safely.
license: MIT
compatibility: Agent Skills (agentskills.io). Funciona em Claude, ChatGPT, Codex, Cursor, Copilot e agentes compatíveis.
metadata:
  author: José Carlos Amorim, Hermes Agent
  version: 0.4.0
  hub: https://agentflix.nexialismo.ai
  source: https://github.com/jcarlosamorim/hermes-skills/tree/main/skills/google-oauth-onboarding
  tags: Google, OAuth, Gmail, Workspace, onboarding
---

# Google OAuth onboarding

Use this skill to connect a student's Google account with minimum necessary access. It works for someone who has never used Google Cloud and for someone who already has a project. It does not send email, create events or change Google data as part of authorization.

## When to use

- The student needs Gmail, Calendar, Drive, Contacts, Docs or Sheets access.
- An existing token expired, lacks a scope or has no refresh token.
- The student needs a consent link from Hermes.
- Do not use API keys for private Gmail or Workspace data.
- Do not use a service account for personal Gmail unless a Workspace administrator explicitly configured domain wide delegation.

## Scope first

Ask which action the student wants, then request only its scope.

| Need | Scope |
| --- | --- |
| Send email | `https://www.googleapis.com/auth/gmail.send` |
| Read email | `https://www.googleapis.com/auth/gmail.readonly` |
| Draft and send email | `https://www.googleapis.com/auth/gmail.compose` |
| Read Calendar | `https://www.googleapis.com/auth/calendar.readonly` |
| Create Calendar events | `https://www.googleapis.com/auth/calendar.events` |
| Read Drive files | `https://www.googleapis.com/auth/drive.readonly` |
| Read Contacts | `https://www.googleapis.com/auth/contacts.readonly` |

Never add mailbox reading to an email sending request. `gmail.send` is sensitive, but narrower than `gmail.modify` or full mail access.

## Branch A: no Google Cloud project

1. Open [Google Cloud](https://console.cloud.google.com/projectselector2/home/dashboard), create a project and select it. Completion: the project name is visible in the console header.
2. Open [Google Auth Platform](https://console.cloud.google.com/auth/overview), configure branding and audience. Use Internal only for a Workspace organization that owns the app. Use External for personal Gmail or external users. Completion: the consent application exists.
3. For an External app in Testing, open [Audience](https://console.cloud.google.com/auth/audience) and add the student's Google account as a test user. Completion: the account appears in Test users.
4. Open the [API Library](https://console.cloud.google.com/apis/library), enable only the needed API. Completion: the API page shows Manage instead of Enable.
5. Open [OAuth clients](https://console.cloud.google.com/auth/clients), create a **Desktop app** client called `Hermes <service>`. Completion: a client ID is listed.
6. Download the client JSON and store it with owner only permissions. Never paste its secret in chat, issue, document or agent memory.

## Branch B: existing Google Cloud project

1. Open [OAuth clients](https://console.cloud.google.com/auth/clients), identify a Desktop app client owned by the same person or organization. Completion: the client and project are identified without exposing its secret.
2. Enable the missing API in the [API Library](https://console.cloud.google.com/apis/library), if needed. Completion: its page shows Manage.
3. Confirm the app audience in [Google Auth Platform](https://console.cloud.google.com/auth/overview). If External and Testing, add the authorizing account in [Audience](https://console.cloud.google.com/auth/audience). Completion: consent is allowed for that account.
4. Reuse a client only when its redirect model is compatible. Otherwise create a dedicated Desktop app client. Completion: one client is explicitly selected.

## Authorization procedure

1. Use `terminal` to verify the client JSON exists, parses and is owner only. Report only existence, mode and client type. Completion: no client secret is printed.
2. Generate a unique PKCE verifier, SHA256 S256 challenge and state for every attempt. Store state and verifier in an owner only pending file. Completion: pending data is not logged or stored in agent memory.
3. Generate the Google consent link with the selected client ID, requested scope, `access_type=offline`, `prompt=consent` and S256 challenge. Send it only through the authorized student channel. Completion: the student can open Google consent.
4. Explain that `http://localhost:1/` can show a browser error after approval. This is expected in a headless flow. The returned URL contains one time authorization material. Treat it as secret and accept it only through an approved private input path. Completion: no code is put in a public issue, document or group.
5. Check the returned state exactly against the pending state, then exchange the code once with the stored verifier. Completion: the token endpoint succeeds.
6. Store the refreshable token in an owner only file. Delete the pending state file. Keep the client secret separate from the token. Completion: token permissions are `0600` on POSIX.
7. Verify granted scopes from token introspection or token response. Do not use a read endpoint to verify a send only token. Completion: every requested scope is present.

## Reauthorization

```text
401 or invalid_grant
  -> refresh token if available
  -> refresh failed: start new consent

403 insufficient permission
  -> inspect granted scopes
  -> request only the missing scope
  -> preserve separate read only tokens when possible

access_denied
  -> External Testing app: add the account as test user
  -> Workspace organization: ask administrator about allowlisting

redirect_uri_mismatch
  -> use redirect compatible with selected client
  -> start a fresh authorization after correcting it
```

## Pitfalls

- A Google API key does not grant access to private Google data.
- A client ID identifies an app. It does not authorize access to a person's account.
- Authorization codes are single use and short lived.
- Public apps using sensitive or restricted scopes can require Google verification for broad distribution. A Testing app is only for its registered test users.
- Authorization is separate from action. Never send email, create an event, modify Drive or import contacts automatically after consent.

## Verification

Before reporting success, prove all items:

- The needed API is enabled.
- OAuth client type is compatible with the flow.
- The student completed consent.
- Returned state matched pending state.
- Token exchange succeeded.
- Granted scope includes every requested scope and no unapproved broad scope.
- Token file is owner only.
- Pending verifier and state were deleted.
