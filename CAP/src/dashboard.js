import React, { useState, useRef, useEffect } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, ResponsiveContainer, XAxis, YAxis, Tooltip, Legend } from 'recharts';
import { AppBar, Toolbar, Typography, Button, Card, CardHeader, CardContent } from '@mui/material';
import { Responsive, WidthProvider } from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';
import 'react-resizable/css/styles.css';

const ResponsiveGridLayout = WidthProvider(Responsive);

const sentimentData = [
  { name: 'Jan', positive: 4000, negative: 2400 },
  { name: 'Feb', positive: 3000, negative: 1398 },
  { name: 'Mar', positive: 2000, negative: 9800 },
  { name: 'Apr', positive: 2780, negative: 3908 },
];

const economicData = [
  { name: '2018', deficit: 3000 },
  { name: '2019', deficit: 2000 },
  { name: '2020', deficit: 2780 }
];

const disasterData = [
  { name: 'Floods', value: 400 },
  { name: 'Earthquakes', value: 300 },
  { name: 'Hurricanes', value: 300 },
  { name: 'Wildfires', value: 200 },
];

const Dashboard = () => {
  const [currentView, setCurrentView] = useState('all');

  const layout = [
    { i: 'sentiments', x: 0, y: 0, w: 1, h: 2 },
    { i: 'economic', x: 1, y: 0, w: 1, h: 2 },
    { i: 'disasters', x: 2, y: 0, w: 1, h: 2 },
    { i: 'opinion', x: 0, y: 2, w: 1, h: 1 },
    { i: 'legislative', x: 1, y: 2, w: 1, h: 1 },
    { i: 'spending', x: 2, y: 2, w: 1, h: 1 },
  ];

  const renderCard = (cardId) => {
    const cardRef = useRef(null);
    const [dimensions, setDimensions] = useState({ width: 0, height: 0 });

    useEffect(() => {
      if (cardRef.current) {
        const resizeObserver = new ResizeObserver(entries => {
          for (const entry of entries) {
            const { width, height } = entry.contentRect;
            setDimensions({ width, height: height - 60 }); // Subtracting header height
          }
        });

        resizeObserver.observe(cardRef.current);

        return () => {
          resizeObserver.disconnect();
        };
      }
    }, []);

    const renderChart = () => {
      switch (cardId) {
        case 'sentiments':
          return (
            <BarChart width={dimensions.width} height={dimensions.height} data={sentimentData}>
              <XAxis dataKey="name" stroke="#fff" />
              <YAxis stroke="#fff" />
              <Tooltip contentStyle={{ backgroundColor: '#333', border: 'none' }} />
              <Bar dataKey="positive" fill="#8884d8" />
              <Bar dataKey="negative" fill="#82ca9d" />
            </BarChart>
          );
        case 'economic':
          return (
            <LineChart width={dimensions.width} height={dimensions.height} data={economicData}>
              <XAxis dataKey="name" stroke="#fff" />
              <YAxis stroke="#fff" />
              <Tooltip contentStyle={{ backgroundColor: '#333', border: 'none' }} />
              <Line type="monotone" dataKey="deficit" stroke="#8884d8" />
            </LineChart>
          );
        case 'disasters':
          return (
            <PieChart width={dimensions.width} height={dimensions.height}>
              <Pie dataKey="value" data={disasterData} fill="#8884d8" label />
              <Tooltip contentStyle={{ backgroundColor: '#333', border: 'none' }} />
            </PieChart>
          );
        // ... Add cases for 'opinion', 'legislative', and 'spending' ...
        default:
          return null;
      }
    };

    return (
      <Card className="bg-gray-800 border-gray-700" ref={cardRef}>
        <CardHeader>{renderChart().props.children[0].props.children}</CardHeader>
        <CardContent>
          {renderChart()}
        </CardContent>
      </Card>
    );
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Civics Analytics Platform
          </Typography>
          <Button color="inherit" onClick={() => setCurrentView('all')}>All</Button>
          <Button color="inherit" onClick={() => setCurrentView('sentiments')}>National Sentiments</Button>
          <Button color="inherit" onClick={() => setCurrentView('economic')}>Economic Statistics</Button>
          <Button color="inherit" onClick={() => setCurrentView('disasters')}>National Disasters</Button>
        </Toolbar>
      </AppBar>
      <div className="p-8">
        <ResponsiveGridLayout
          className="layout"
          layouts={{ lg: layout }}
          breakpoints={{ lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }}
          cols={{ lg: 3, md: 2, sm: 1, xs: 1, xxs: 1 }}
          rowHeight={300}
        >
          {layout.map(item => (
            <div key={item.i} style={{ display: currentView === 'all' || currentView === item.i ? 'block' : 'none' }}>
              {renderCard(item.i)}
            </div>
          ))}
        </ResponsiveGridLayout>
      </div>
    </div>
  );
};

export default Dashboard;