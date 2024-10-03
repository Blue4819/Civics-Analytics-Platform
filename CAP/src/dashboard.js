import React from 'react'
import { BarChart, Bar, LineChart, Line, PieChart, Pie, ResponsiveContainer, XAxis, YAxis, Tooltip, Legend } from 'recharts'
import { Paper, Typography } from '@mui/material';

const CardHeader = ({ children }) => {
  return (
    <div style={{ padding: '16px', borderBottom: '1px solid #ccc' }}>
      <Typography variant="h6">{children}</Typography>
    </div>
  );
};

const CardContent = ({ children }) => {
  return (
    <div style={{ padding: '16px' }}>
      {children}
    </div>
  );
};

const Card = ({ children, className }) => {
  return (
    <Paper elevation={0} className={className} style={{ borderRadius: '8px', overflow: 'hidden' }}>
      {children}
    </Paper>
  );
};

const sentimentData = [
  { name: 'Jan', positive: 4000, negative: 2400 },
  { name: 'Feb', positive: 3000, negative: 1398 },
  { name: 'Mar', positive: 2000, negative: 9800 },
  { name: 'Apr', positive: 2780, negative: 3908 },
  { name: 'May', positive: 1890, negative: 4800 },
  { name: 'Jun', positive: 2390, negative: 3800 },
]

const economicData = [
  { name: 'Q1', deficit: 2400 },
  { name: 'Q2', deficit: 1398 },
  { name: 'Q3', deficit: 9800 },
  { name: 'Q4', deficit: 3908 },
]

const disasterData = [
  { name: 'Floods', value: 400 },
  { name: 'Earthquakes', value: 300 },
  { name: 'Hurricanes', value: 300 },
  { name: 'Wildfires', value: 200 },
]

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-900 p-8 text-white">
      <h1 className="text-4xl font-bold mb-8 text-center">Civics Analytics Platform</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* National Sentiments */}
        <Card className="bg-gray-800 border-gray-700">
          <CardHeader>National Sentiments</CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={sentimentData}>
                <XAxis dataKey="name" stroke="#fff" />
                <YAxis stroke="#fff" />
                <Tooltip contentStyle={{ backgroundColor: '#333', border: 'none' }} />
                <Bar dataKey="positive" fill="#8884d8" />
                <Bar dataKey="negative" fill="#82ca9d" />
              </BarChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* Economic Fiscal Deficits */}
        <Card className="bg-gray-800 border-gray-700">
          <CardHeader>Economic Fiscal Deficits</CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={200}>
              <LineChart data={economicData}>
                <XAxis dataKey="name" stroke="#fff" />
                <YAxis stroke="#fff" />
                <Tooltip contentStyle={{ backgroundColor: '#333', border: 'none' }} />
                <Line type="monotone" dataKey="deficit" stroke="#8884d8" />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* National Disasters */}
        <Card className="bg-gray-800 border-gray-700">
          <CardHeader>National Disasters</CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie dataKey="value" data={disasterData} fill="#8884d8" label />
                <Tooltip contentStyle={{ backgroundColor: '#333', border: 'none' }} />
              </PieChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        {/* Additional cards for more metrics */}
        <Card className="bg-gray-800 border-gray-700">
          <CardHeader>Public Opinion</CardHeader>
          <CardContent>
            <div className="text-6xl font-bold text-center">67%</div>
            <div className="text-center text-gray-400">Approval Rating</div>
          </CardContent>
 </Card>

        <Card className="bg-gray-800 border-gray-700">
          <CardHeader>Legislative Productivity</CardHeader>
          <CardContent>
            <div className="text-6xl font-bold text-center">85</div>
            <div className="text-center text-gray-400">Bills Passed</div>
          </CardContent>
        </Card>

        <Card className="bg-gray-800 border-gray-700">
          <CardHeader>Government Spending</CardHeader>
          <CardContent>
            <div className="text-6xl font-bold text-center">$1.2T</div>
            <div className="text-center text-gray-400">Total Spending</div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}