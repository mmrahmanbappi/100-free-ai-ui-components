# 100 Free AI UI Components

![Free AI UI components](_site/og-home.jpg)

The parts every AI app needs: prompt boxes, thinking animations, token meters, answer ratings, agent tool calls and more. Each component is one HTML file with plain CSS and JavaScript. No library, no build step.

**[See every component with a live demo](https://mmrahmanbappi.github.io/100-free-ai-ui-components/)**

40 of 100 components are ready. New ones are added every week.

## Why use these components

- **One file each.** Copy it into any site, or move the markup into React, Vue or Svelte.
- **Light and dark mode.** Follows the device setting automatically.
- **Accessible.** Keyboard support and labels for screen readers.
- **Works on phones.** Every component fits small screens.
- **Easy to rebrand.** Change `--accent` at the top of the CSS.
- **Free for business use.** MIT license.

## How to use a component

1. Open the [website](https://mmrahmanbappi.github.io/100-free-ai-ui-components/) and pick a component.
2. Try the live demo in light and dark mode.
3. Click **Copy the code** or **Download the file**, then connect it to your AI service.

The components are the interface only. They do not call any AI model, so you can use them with any provider.

## Components

### Prompt Input

Boxes where people type to the AI, from a simple field to slash commands and history.

| Preview | Component |
|---|---|
| [![Basic Prompt Box](prompt-input/basic-prompt-box/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/basic-prompt-box/) | **[Basic Prompt Box](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/basic-prompt-box/)**<br>A clean prompt box. Enter sends, Shift and Enter adds a new line, and the send button stays off until there is text. |
| [![Auto-Growing Prompt](prompt-input/auto-grow-prompt/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/auto-grow-prompt/) | **[Auto-Growing Prompt](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/auto-grow-prompt/)**<br>A prompt that grows as people type, stops at a set height and then scrolls. Shows a live character count. |
| [![Prompt with File Attachments](prompt-input/prompt-with-attachments/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-with-attachments/) | **[Prompt with File Attachments](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-with-attachments/)**<br>Attach files with a button or by dragging them onto the box. Each file shows as a chip with its size and a remove button. |
| [![Prompt with Voice Input](prompt-input/voice-input-prompt/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/voice-input-prompt/) | **[Prompt with Voice Input](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/voice-input-prompt/)**<br>A microphone button that turns speech into text when the browser supports it, with a pulsing record state and a timer. |
| [![Prompt with Slash Commands](prompt-input/slash-commands-prompt/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/slash-commands-prompt/) | **[Prompt with Slash Commands](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/slash-commands-prompt/)**<br>Type a slash to open a command menu. Use the arrow keys to move, Enter to pick, and Escape to close. |
| [![Prompt with Model Picker](prompt-input/model-picker-prompt/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/model-picker-prompt/) | **[Prompt with Model Picker](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/model-picker-prompt/)**<br>A prompt box with a small menu to choose how the AI should answer: fast, balanced or deep thinking. |
| [![Prompt Suggestions](prompt-input/prompt-suggestions/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-suggestions/) | **[Prompt Suggestions](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-suggestions/)**<br>Starter ideas shown as buttons above an empty prompt. Clicking one fills the box so people can edit it before sending. |
| [![Prompt with Token Counter](prompt-input/prompt-token-counter/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-token-counter/) | **[Prompt with Token Counter](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-token-counter/)**<br>Estimates how many tokens a prompt will use as people type, with a bar that turns orange and then red near the limit. |
| [![Prompt with Send Shortcut Setting](prompt-input/send-shortcut-prompt/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/send-shortcut-prompt/) | **[Prompt with Send Shortcut Setting](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/send-shortcut-prompt/)**<br>Lets people choose whether Enter sends the message or adds a new line, with a keyboard hint that updates to match. |
| [![Prompt with History](prompt-input/prompt-history/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-history/) | **[Prompt with History](https://mmrahmanbappi.github.io/100-free-ai-ui-components/prompt-input/prompt-history/)**<br>Press the Up arrow in an empty box to bring back earlier prompts, like a terminal. Recent prompts also appear as a list. |

### Thinking and Loading

Animations and states that show the AI is working, streaming or using a tool.

| Preview | Component |
|---|---|
| [![Typing Dots](thinking/typing-dots/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/typing-dots/) | **[Typing Dots](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/typing-dots/)**<br>Three bouncing dots inside an answer bubble, the classic sign that the AI is writing a reply. |
| [![Thinking Shimmer](thinking/thinking-shimmer/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/thinking-shimmer/) | **[Thinking Shimmer](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/thinking-shimmer/)**<br>A soft light moves across the word Thinking while the AI works, then it changes to how long the thinking took. |
| [![Streaming Text](thinking/streaming-text/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/streaming-text/) | **[Streaming Text](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/streaming-text/)**<br>The answer appears word by word with a blinking cursor, the way most AI chat apps show a reply as it is written. |
| [![Reasoning Panel](thinking/reasoning-panel/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/reasoning-panel/) | **[Reasoning Panel](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/reasoning-panel/)**<br>A panel that shows each thinking step while the AI works, then folds itself away with a summary you can open again. |
| [![Agent Progress Steps](thinking/agent-progress-steps/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/agent-progress-steps/) | **[Agent Progress Steps](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/agent-progress-steps/)**<br>A checklist of what an AI agent is doing right now. Each step shows a spinner while it runs and a tick when it is done. |
| [![Skeleton Message](thinking/skeleton-message/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/skeleton-message/) | **[Skeleton Message](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/skeleton-message/)**<br>Grey placeholder lines with a moving shine that hold the space of the answer while it loads, so the page does not jump. |
| [![AI Orb](thinking/ai-orb/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/ai-orb/) | **[AI Orb](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/ai-orb/)**<br>A glowing orb that shows what the assistant is doing: resting, listening or thinking. Great for voice and assistant screens. |
| [![Spinner with Status Text](thinking/status-spinner/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/status-spinner/) | **[Spinner with Status Text](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/status-spinner/)**<br>A small spinner with a line of text that changes as the work moves forward, so people know the AI has not frozen. |
| [![Web Search Indicator](thinking/tool-call-indicator/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/tool-call-indicator/) | **[Web Search Indicator](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/tool-call-indicator/)**<br>Shows that the AI is searching the web, with sources popping in one by one, then a short summary of how many it found. |
| [![Stop Generating Button](thinking/stop-generating/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/stop-generating/) | **[Stop Generating Button](https://mmrahmanbappi.github.io/100-free-ai-ui-components/thinking/stop-generating/)**<br>A stop button that appears while the answer is being written. Stopping keeps what was written and offers to continue or try again. |

### Chat Messages

Message bubbles, code blocks, sources and actions for AI answers.

| Preview | Component |
|---|---|
| [![Chat Bubbles](messages/chat-bubbles/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/chat-bubbles/) | **[Chat Bubbles](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/chat-bubbles/)**<br>A simple conversation with user and assistant bubbles, avatars and times. The user sits on the right in the brand color. |
| [![Formatted Answer](messages/formatted-answer/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/formatted-answer/) | **[Formatted Answer](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/formatted-answer/)**<br>A styled answer with headings, lists, bold text, inline code, a quote and a table, ready for text your AI returns as Markdown. |
| [![Code Block with Copy Button](messages/code-block-copy/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/code-block-copy/) | **[Code Block with Copy Button](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/code-block-copy/)**<br>A code block with a language label, a copy button that confirms when done, and a button to wrap long lines. |
| [![Message Action Bar](messages/message-actions/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/message-actions/) | **[Message Action Bar](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/message-actions/)**<br>A row of actions under an answer: copy the text, read it aloud with the browser voice, and share it. |
| [![Answer Versions](messages/answer-versions/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/answer-versions/) | **[Answer Versions](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/answer-versions/)**<br>Regenerate an answer and move between versions with small arrows showing 1 of 3, like popular chat apps do. |
| [![Inline Citations](messages/inline-citations/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/inline-citations/) | **[Inline Citations](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/inline-citations/)**<br>Numbered source markers inside an answer. Hover or focus a number to see the source, and find the full list below. |
| [![Editable User Message](messages/edit-message/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/edit-message/) | **[Editable User Message](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/edit-message/)**<br>An edit button on the user message turns it into a text box with Save and Cancel, so people can fix a question and ask again. |
| [![Error Message with Retry](messages/error-retry/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/error-retry/) | **[Error Message with Retry](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/error-retry/)**<br>A clear error in the chat when an answer fails, with a Retry button that shows progress and then the answer. |
| [![Message with Attached Files](messages/file-message/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/file-message/) | **[Message with Attached Files](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/file-message/)**<br>A user message with attached file cards, showing the file type, name and size, followed by the assistant's reply. |
| [![Long Answer with Show More](messages/long-message-toggle/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/long-message-toggle/) | **[Long Answer with Show More](https://mmrahmanbappi.github.io/100-free-ai-ui-components/messages/long-message-toggle/)**<br>Long answers fold after a few lines with a soft fade and a Show more button, so the chat stays easy to scan. |

### Answer Feedback

Ratings, thumbs, comparisons and forms that tell you if an answer helped.

| Preview | Component |
|---|---|
| [![Thumbs Up and Down](feedback/thumbs-feedback/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/thumbs-feedback/) | **[Thumbs Up and Down](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/thumbs-feedback/)**<br>Two small buttons under an answer. Pick one to rate it, pick it again to undo, and see a short thank you. |
| [![Thumbs Down with Reasons](feedback/thumbs-down-reasons/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/thumbs-down-reasons/) | **[Thumbs Down with Reasons](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/thumbs-down-reasons/)**<br>When someone marks an answer as bad, a small panel asks why, with quick reason buttons and an optional comment. |
| [![Star Rating](feedback/star-rating/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/star-rating/) | **[Star Rating](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/star-rating/)**<br>Rate an answer from one to five stars with the mouse or keyboard. Each level shows a word, like Good or Excellent. |
| [![Was This Helpful Bar](feedback/helpful-bar/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/helpful-bar/) | **[Was This Helpful Bar](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/helpful-bar/)**<br>A short question at the end of an answer with Yes and No buttons. It turns into a thank you once someone answers. |
| [![Compare Two Answers](feedback/compare-answers/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/compare-answers/) | **[Compare Two Answers](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/compare-answers/)**<br>Two answers side by side so people can pick the better one, or say both are good or both are bad. Useful for testing models. |
| [![Report a Problem Dialog](feedback/report-dialog/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/report-dialog/) | **[Report a Problem Dialog](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/report-dialog/)**<br>A report button opens a dialog to flag an answer, with categories and details. It traps focus and closes with Escape. |
| [![Satisfaction Scale](feedback/satisfaction-scale/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/satisfaction-scale/) | **[Satisfaction Scale](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/satisfaction-scale/)**<br>Five faces from very unhappy to very happy. A quick way to ask how a chat went, drawn in SVG so it looks the same everywhere. |
| [![Rewrite Options Menu](feedback/rewrite-options/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/rewrite-options/) | **[Rewrite Options Menu](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/rewrite-options/)**<br>A Try again button with a menu to change the answer: shorter, longer, simpler or more formal. The answer updates in place. |
| [![Confidence Badge](feedback/confidence-badge/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/confidence-badge/) | **[Confidence Badge](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/confidence-badge/)**<br>A small badge that tells people how sure the AI is about an answer, with a short explanation and a reminder to check sources. |
| [![Feedback Toast with Undo](feedback/feedback-toast/thumb.webp)](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/feedback-toast/) | **[Feedback Toast with Undo](https://mmrahmanbappi.github.io/100-free-ai-ui-components/feedback/feedback-toast/)**<br>After someone rates an answer, a small message slides up to confirm it, with an Undo button for a few seconds. |

## Coming next

Tokens and Usage, Model and Settings, Chat Layouts, Agents and Tools, Voice and Media, Trust and Onboarding.

## License

[MIT](LICENSE). Free for personal and business use.

Made by [MM Rahman Bappi](https://mmseo.app/).
