import { vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Table } from '@mui/material';
import EnhancedTableHead, { headCells } from './TableHead';
import userEvent from '@testing-library/user-event';

let updateMethod = vi.fn();

describe('TableHead', () => {
  afterAll(() => {
    updateMethod.mockRestore();
  });
  it('renders all cells', async () => {
    render(
      <Table>
        <EnhancedTableHead order="asc" setOrder={updateMethod} />
      </Table>,
    );

    headCells.map((cell) =>
      expect(screen.queryByText(cell.label)).toBeInTheDocument(),
    );
  });
  it('on click changes sort order', async () => {
    const user = userEvent.setup();
    render(
      <Table>
        <EnhancedTableHead order="asc" setOrder={updateMethod} />
      </Table>,
    );

    await user.click(screen.getByText('Gold'));
    expect(updateMethod).toHaveBeenCalledWith('desc');
  });
  it('on click changes sort order reverse', async () => {
    const user = userEvent.setup();
    render(
      <Table>
        <EnhancedTableHead order="desc" setOrder={updateMethod} />
      </Table>,
    );

    await user.click(screen.getByText('Gold'));
    expect(updateMethod).toHaveBeenCalledWith('asc');
  });
});
