import { Dispatch, SetStateAction } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import React from 'react';

interface CustomSelectProps {
  values: string[];
  activeValue: string;
  label: string;
  setValue: Dispatch<SetStateAction<string>>;
}

const CustomSelect: React.FC<CustomSelectProps> = ({
  activeValue,
  values,
  label,
  setValue,
}) => {
  const handleChange = (event: SelectChangeEvent) => {
    setValue(event.target.value as string);
  };
  // N.B. If multiple selects have the same label on the same page this may cause issues
  const labelId = `${label.replace(' ', '-')}`;

  return (
    <FormControl
      variant="filled"
      sx={{ m: 1, minWidth: 120, backgroundColor: 'white' }}
      size="small"
    >
      <InputLabel id={labelId}>{label}</InputLabel>
      <Select
        data-testid="select-element"
        value={activeValue}
        label={label}
        onChange={handleChange}
        labelId={labelId}
      >
        {values.map((value) => (
          <MenuItem key={value} value={value}>
            {value}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};

export default CustomSelect;
