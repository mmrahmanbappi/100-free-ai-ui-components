# 100 Free AI UI Components

![Free AI UI components](_site/og-home.jpg)

The parts every AI app needs: prompt boxes, thinking animations, token meters, answer ratings, agent tool calls and more. Each component is one HTML file with plain CSS and JavaScript. No library, no build step.

**[See every component with a live demo](https://mmrahmanbappi.github.io/100-free-ai-ui-components/)**

20 of 100 components are ready. New ones are added every week.

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

## Coming next

Chat Messages, Answer Feedback, Tokens and Usage, Model and Settings, Chat Layouts, Agents and Tools, Voice and Media, Trust and Onboarding.

## License

[MIT](LICENSE). Free for personal and business use.

Made by [MM Rahman Bappi](https://mmseo.app/).
