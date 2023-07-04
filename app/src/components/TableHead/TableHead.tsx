import React, { Dispatch, SetStateAction } from 'react';
import Box from '@mui/material/Box';

import TableCell from '@mui/material/TableCell';

import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import TableSortLabel from '@mui/material/TableSortLabel';

import { visuallyHidden } from '@mui/utils';
import { CountryData, SortOrder } from '../Table/Table';

interface HeadCell {
  disablePadding: boolean;
  id: keyof CountryData | 'flag';
  label: string;
  numeric: boolean;
  sortable: boolean;
}

export const headCells: readonly HeadCell[] = [
  {
    id: 'flag',
    sortable: false,
    numeric: false,
    disablePadding: false,
    label: 'Flag',
  },
  {
    id: 'country_name',
    sortable: false,
    numeric: false,
    disablePadding: true,
    label: 'Country Name',
  },
  {
    id: 'country_code',
    sortable: false,
    numeric: false,
    disablePadding: false,
    label: 'Country Code',
  },
  {
    id: 'gold_medal_count',
    sortable: true,
    numeric: true,
    disablePadding: false,
    label: 'Gold',
  },
  {
    id: 'silver_medal_count',
    sortable: false,
    numeric: true,
    disablePadding: false,
    label: 'Silver',
  },
  {
    id: 'bronze_medal_count',
    sortable: false,
    numeric: true,
    disablePadding: false,
    label: 'Bronze',
  },
];

interface EnhancedTableHeadProps {
  order: SortOrder;
  setOrder: Dispatch<SetStateAction<SortOrder>>;
}

const EnhancedTableHead: React.FC<EnhancedTableHeadProps> = ({
  order, // Order direction for UI
  setOrder,
}) => {
  const createSortHandler = () => () => {
    const newOrder = order === 'desc' ? 'asc' : 'desc';
    setOrder(newOrder);
  };

  const orderBy = 'gold_medal_count'; // This could be easily abstracted to allowing sorting by other columns

  return (
    <TableHead>
      <TableRow>
        {headCells.map((headCell) => (
          <TableCell
            key={headCell.id}
            align={headCell.numeric ? 'right' : 'left'}
            padding={headCell.disablePadding ? 'none' : 'normal'}
            sortDirection={orderBy === headCell.id ? order : false}
          >
            {(headCell.sortable && (
              <TableSortLabel
                active={orderBy === headCell.id}
                direction={orderBy === headCell.id ? order : 'asc'}
                onClick={createSortHandler()}
              >
                {headCell.label}
                {orderBy === headCell.id ? (
                  <Box component="span" sx={visuallyHidden}>
                    {order === 'desc'
                      ? 'sorted descending'
                      : 'sorted ascending'}
                  </Box>
                ) : null}
              </TableSortLabel>
            )) ||
              headCell.label}
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
};

export default EnhancedTableHead;
