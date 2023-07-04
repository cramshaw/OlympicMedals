# Olympic Medal Frontend

This is a [Vite.js](https://vitejs.dev/) based React application providing a frontend for Olympic Medal table.

Commands can be found in `package.json` but details on how to get started are below.

## Quick Start

1. Ensure that the backend application is running.

2. The simplest way to run the application is using npm. Assuming you have the correct version of node, start by installing the dependencies with:

```
npm install
```

3. Then to start the dev server:

```
npm run dev
```

This will start a dev server and server the application at [http://localhost:5173/](http://localhost:5173/).

## Development

Tests are setup using the [Vitest](https://vitest.dev/) framework and React Testing Library. This works in very similar way to Jest. To run, it's a simple:

```
npm run test
```

## Building

It is possible to bundle a build of the application simply by running

```
npm run build
```

## Notes

- Node has been bumped to the latest LTS (18.16)
- Flag emojis are not perfect but provide solid coverage for most countries.
