import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import EnhancedTableHead from '../TableHead/TableHead';
import getUnicodeFlagIcon from 'country-flag-icons/unicode';
import flagMap from './flagMap.json';

// Our country codes don't quite match up so we have a mapping file
const _flagMap = flagMap as Record<string, string>;

export type CountryData = {
  country_code: string;
  country_name: string;
  gold_medal_count: number;
  silver_medal_count: number;
  bronze_medal_count: number;
};

export type SortOrder = 'asc' | 'desc';

interface EnhancedTableProps {
  data: CountryData[];
}

export const sortMedals = (obj1: CountryData, obj2: CountryData) => {
  return (
    obj2.gold_medal_count - obj1.gold_medal_count ||
    obj2.silver_medal_count - obj1.silver_medal_count ||
    obj2.bronze_medal_count - obj1.bronze_medal_count
  );
};

const EnhancedTable: React.FC<EnhancedTableProps> = ({ data }) => {
  const [order, setOrder] = useState<SortOrder>('desc');

  const sortedRows = React.useMemo(
    () =>
      data.sort((obj1: CountryData, obj2: CountryData) => {
        return (
          (order == 'desc' && sortMedals(obj1, obj2)) || sortMedals(obj2, obj1)
        );
      }),
    [order, data],
  );

  return (
    <Box sx={{ width: '100%' }}>
      <Paper sx={{ width: '100%', mb: 2 }}>
        <TableContainer>
          <Table aria-labelledby="dataTable">
            <EnhancedTableHead order={order} setOrder={setOrder} />
            <TableBody>
              {sortedRows.map((row) => {
                return (
                  <TableRow
                    hover
                    key={row.country_code}
                    data-testid="enhancedTableRow"
                  >
                    <TableCell align="left">
                      {getUnicodeFlagIcon(
                        _flagMap[row.country_code] || row.country_code,
                      )}
                    </TableCell>
                    <TableCell align="left">{row.country_code}</TableCell>
                    <TableCell align="left">{row.country_name}</TableCell>
                    <TableCell align="right">{row.gold_medal_count}</TableCell>
                    <TableCell align="right">
                      {row.silver_medal_count}
                    </TableCell>
                    <TableCell align="right">
                      {row.bronze_medal_count}
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </Box>
  );
};

export default EnhancedTable;
