import { render, screen } from '@testing-library/react';
import { Table } from '@mui/material';
import userEvent from '@testing-library/user-event';
import EnhancedTable, { sortMedals } from './Table';

const data = [
  {
    country_name: 'France',
    country_code: 'FRA',
    gold_medal_count: 1,
    silver_medal_count: 2,
    bronze_medal_count: 2,
  },
  {
    country_name: 'Germany',
    country_code: 'DEU',
    gold_medal_count: 3,
    silver_medal_count: 2,
    bronze_medal_count: 2,
  },
  {
    country_name: 'Argentina',
    country_code: 'ARG',
    gold_medal_count: 1,
    silver_medal_count: 1,
    bronze_medal_count: 2,
  },
];

describe('Table', () => {
  it('renders all data', () => {
    render(<EnhancedTable data={data} />);

    const row1 = screen.getByText('Argentina');
    expect(row1).toBeInTheDocument();
    const row2 = screen.getByText('France');
    expect(row2).toBeInTheDocument();
    const row3 = screen.getByText('Germany');
    expect(row3).toBeInTheDocument();
  });
  it('renders sorted data', () => {
    render(<EnhancedTable data={data} />);
    // Ensure Germany is top row

    const rows = screen.getAllByTestId('enhancedTableRow');

    expect(rows).toHaveLength(3);

    expect(rows[0]).toHaveTextContent('Germany');
    expect(rows[1]).toHaveTextContent('France');
    expect(rows[2]).toHaveTextContent('Argentina');
  });
  it('sortMedals works asc', () => {
    it('sorts by gold medal'),
      () => {
        expect(
          sortMedals(
            {
              country_name: 'France',
              country_code: 'FRA',
              gold_medal_count: 1,
              silver_medal_count: 0,
              bronze_medal_count: 0,
            },
            {
              country_name: 'Argentina',
              country_code: 'ARG',
              gold_medal_count: 0,
              silver_medal_count: 0,
              bronze_medal_count: 0,
            },
          ),
        ).toBe(-1);
      };
    it('sorts by silver medal'),
      () => {
        expect(
          sortMedals(
            {
              country_name: 'France',
              country_code: 'FRA',
              gold_medal_count: 1,
              silver_medal_count: 1,
              bronze_medal_count: 0,
            },
            {
              country_name: 'Argentina',
              country_code: 'ARG',
              gold_medal_count: 1,
              silver_medal_count: 0,
              bronze_medal_count: 0,
            },
          ),
        ).toBe(-1);
      };
    it('sorts by bronze medal'),
      () => {
        expect(
          sortMedals(
            {
              country_name: 'France',
              country_code: 'FRA',
              gold_medal_count: 1,
              silver_medal_count: 1,
              bronze_medal_count: 1,
            },
            {
              country_name: 'Argentina',
              country_code: 'ARG',
              gold_medal_count: 1,
              silver_medal_count: 1,
              bronze_medal_count: 0,
            },
          ),
        ).toBe(-1);
      };
  });
  it('sortMedals works desc', () => {
    it('sorts by gold medal'),
      () => {
        expect(
          sortMedals(
            {
              country_name: 'Argentina',
              country_code: 'ARG',
              gold_medal_count: 0,
              silver_medal_count: 0,
              bronze_medal_count: 0,
            },
            {
              country_name: 'France',
              country_code: 'FRA',
              gold_medal_count: 1,
              silver_medal_count: 0,
              bronze_medal_count: 0,
            },
          ),
        ).toBe(1);
      };
    it('sorts by silver medal'),
      () => {
        expect(
          sortMedals(
            {
              country_name: 'Argentina',
              country_code: 'ARG',
              gold_medal_count: 1,
              silver_medal_count: 0,
              bronze_medal_count: 0,
            },
            {
              country_name: 'Argentina',
              country_code: 'ARG',
              gold_medal_count: 1,
              silver_medal_count: 1,
              bronze_medal_count: 0,
            },
          ),
        ).toBe(1);
      };
    it('sorts by bronze medal'),
      () => {
        expect(
          sortMedals(
            {
              country_name: 'Argentina',
              country_code: 'ARG',
              gold_medal_count: 1,
              silver_medal_count: 1,
              bronze_medal_count: 0,
            },
            {
              country_name: 'France',
              country_code: 'FRA',
              gold_medal_count: 1,
              silver_medal_count: 1,
              bronze_medal_count: 1,
            },
          ),
        ).toBe(-1);
      };
  });
  it('flag renders', async () => {
    const data = [
      {
        country_name: 'France',
        country_code: 'FRA',
        gold_medal_count: 1,
        silver_medal_count: 1,
        bronze_medal_count: 1,
      },
    ];
    render(<EnhancedTable data={data} />);

    const flag = screen.getByText('🇫🇷');
    expect(flag).toBeInTheDocument();
  });
});
