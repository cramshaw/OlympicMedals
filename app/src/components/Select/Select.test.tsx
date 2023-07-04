import { vi } from 'vitest';
import { fireEvent, render, screen, within } from '@testing-library/react';
import CustomSelect from './Select';

let updateMethod = vi.fn();

const values = ['2004', '2008', '2012'];

describe('Select', () => {
  afterAll(() => {
    updateMethod.mockRestore();
  });
  it('renders all values', () => {
    render(
      <CustomSelect
        activeValue="2004"
        values={values}
        label="myLabel"
        setValue={updateMethod}
      />,
    );

    const selectEl = screen.getByTestId('select-element');
    const button = within(selectEl).getByRole('button');
    fireEvent.mouseDown(button);
    const listbox = within(screen.getByRole('presentation')).getByRole(
      'listbox',
    );

    const options = within(listbox).getAllByRole('option');
    const optionValues = options.map((li) => li.getAttribute('data-value'));

    expect(optionValues).toEqual(['2004', '2008', '2012']);
  });
  it('fires callback with for selected value', () => {
    render(
      <CustomSelect
        activeValue="2004"
        values={values}
        label="myLabel"
        setValue={updateMethod}
      />,
    );
    const selectEl = screen.getByTestId('select-element');
    const button = within(selectEl).getByRole('button');
    fireEvent.mouseDown(button);
    const listbox = within(screen.getByRole('presentation')).getByRole(
      'listbox',
    );

    const options = within(listbox).getAllByRole('option');

    fireEvent.click(options[2]);
    expect(updateMethod).toHaveBeenCalledWith('2012');
  });
  it('renders label', async () => {
    render(
      <CustomSelect
        activeValue="2004"
        values={values}
        label="myLabel"
        setValue={updateMethod}
      />,
    );

    const selectEl = await screen.findByLabelText(/myLabel/i);

    expect(selectEl).toBeInTheDocument();
  });
});
