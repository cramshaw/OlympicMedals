import { expect, afterEach } from 'vitest';
import { cleanup } from '@testing-library/react';
import matchers from '@testing-library/jest-dom/matchers';
import { setupServer } from 'msw/node'
import { rest } from 'msw'

// extends Vitest's expect method with methods from react-testing-library
expect.extend(matchers);

const data = [
  {
    country_name: 'Argentina',
    country_code: 'ARG',
    gold_medal_count: 1,
    silver_medal_count: 1,
    bronze_medal_count: 2,
  },
];

export const restHandlers = [
  rest.get('http://localhost:8000/api/v1/medal-table/2012/', (req, res, ctx) => {
    return res(ctx.status(200), ctx.json(data));
  }),
];

const server = setupServer(...restHandlers)

// Start server before all tests
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }))

//  Close server after all tests
afterAll(() => server.close())

// runs a cleanup after each test case (e.g. clearing jsdom)
afterEach(() => {
  server.resetHandlers()
  cleanup();
});

export default server;