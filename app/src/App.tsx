import {
  AppBar,
  Box,
  CircularProgress,
  Toolbar,
  Typography,
} from '@mui/material';
import './App.css';
import CustomSelect from './components/Select/Select';
import EnhancedTable from './components/Table/Table';
import { useEffect, useState } from 'react';

function App() {
  const rootDomain = 'http://localhost:8000';

  const [year, setYear] = useState('2012');
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  /* TODO: Load from an API Endpoint */
  const years = ['2004', '2008', '2012'];

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      const response = await fetch(`${rootDomain}/api/v1/medal-table/${year}/`);
      const newData = await response.json();
      setLoading(false);
      setData(newData);
    };

    fetchData();
  }, [year]);

  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h4" component="h1" sx={{ flexGrow: 1 }}>
            Olympic Medal Table
          </Typography>
          <CustomSelect
            label={'Games Year:'}
            values={years}
            activeValue={year}
            setValue={setYear}
          />
        </Toolbar>
      </AppBar>
      <Box sx={{ flexGrow: 1 }}>
        {(!loading && <EnhancedTable data={data} />) || <CircularProgress />}
      </Box>
    </>
  );
}

export default App;
