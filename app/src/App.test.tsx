import { render, screen, waitFor } from '@testing-library/react';
import App from '../src/App';
import server from './test/setup';

describe('App', () => {
  it('renders', async () => {
    server.use();
    render(<App />);

    expect(screen.queryByText(/Olympic Medal Table/i)).toBeInTheDocument();
    expect(screen.queryByText(/2012/i)).toBeInTheDocument();
    await waitFor(() =>
      expect(screen.queryByText(/Argentina/i)).toBeInTheDocument(),
    );
  });
});
