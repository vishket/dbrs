{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# DBRS Technical Assessment"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import Pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 1 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) Load data(2017_SR_Subset) into a dataframe df1\n",
    "\n",
    "2) Fetch 10 common 'complaint_types' and store as a Series\n",
    "\n",
    "3) Filter dataframe rows only if value in 'complaint_type' column is present in series\n",
    "\n",
    "4) Group dataframe rows by 'borough', and for each 'borough', count occurrence of 'top_10_complaint_type'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read csv dataset into a dataframe\n",
    "df = pd.read_csv('2017_SR_subet_vs.csv', low_memory=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2439273 entries, 0 to 2439272\n",
      "Data columns (total 6 columns):\n",
      "Unique Key        int64\n",
      "Created Date      object\n",
      "Complaint Type    object\n",
      "Incident Zip      object\n",
      "City              object\n",
      "Borough           object\n",
      "dtypes: int64(1), object(5)\n",
      "memory usage: 111.7+ MB\n"
     ]
    }
   ],
   "source": [
    "# Inspect dataframe\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df.rename(columns={'Complaint Type': 'complaint_type', 'oldName2': 'newName2'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the 10 common complaint types\n",
    "top_10_complaint_types = df['complaint_type'].value_counts().head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Noise - Residential        230152\n",
       "HEAT/HOT WATER             213521\n",
       "Illegal Parking            146122\n",
       "Blocked Driveway           136096\n",
       "Street Condition            93265\n",
       "Street Light Condition      84195\n",
       "UNSANITARY CONDITION        79282\n",
       "Noise - Street/Sidewalk     73085\n",
       "Water System                65096\n",
       "Noise                       60171\n",
       "Name: complaint_type, dtype: int64"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top_10_complaint_types"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-155-afcb83f45016>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-155-afcb83f45016>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    result1 = df[df.Complaint Type.isin(top_10_Complaint Types.index.tolist())][['BOROUGH', \"Complaint Type\"]].groupby(['BOROUGH', 'Complaint Type'])[\"Complaint Type\"].count()\u001b[0m\n\u001b[0m                                 ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "result1 = df[df.complaint_type.isin(top_10_complaint_types.index.tolist())][['borough', 'complaint_type']].groupby(['borough', 'complaint_type'])['complaint_type'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "borough        complaint_type         \n",
      "BRONX          Blocked Driveway           24574\n",
      "               HEAT/HOT WATER             68718\n",
      "               Illegal Parking            16122\n",
      "               Noise                       3134\n",
      "               Noise - Residential        57663\n",
      "               Noise - Street/Sidewalk    14025\n",
      "               Street Condition           11761\n",
      "               Street Light Condition     18410\n",
      "               UNSANITARY CONDITION       24561\n",
      "               Water System               10217\n",
      "BROOKLYN       Blocked Driveway           49302\n",
      "               HEAT/HOT WATER             66984\n",
      "               Illegal Parking            55380\n",
      "               Noise                      15421\n",
      "               Noise - Residential        67629\n",
      "               Noise - Street/Sidewalk    21313\n",
      "               Street Condition           25432\n",
      "               Street Light Condition     22458\n",
      "               UNSANITARY CONDITION       26659\n",
      "               Water System               19809\n",
      "MANHATTAN      Blocked Driveway            3428\n",
      "               HEAT/HOT WATER             46529\n",
      "               Illegal Parking            19687\n",
      "               Noise                      29002\n",
      "               Noise - Residential        51026\n",
      "               Noise - Street/Sidewalk    29147\n",
      "               Street Condition           14840\n",
      "               Street Light Condition     11077\n",
      "               UNSANITARY CONDITION       14635\n",
      "               Water System               10929\n",
      "QUEENS         Blocked Driveway           54289\n",
      "               HEAT/HOT WATER             29217\n",
      "               Illegal Parking            46065\n",
      "               Noise                      10685\n",
      "               Noise - Residential        46396\n",
      "               Noise - Street/Sidewalk     7530\n",
      "               Street Condition           30629\n",
      "               Street Light Condition     24258\n",
      "               UNSANITARY CONDITION       11474\n",
      "               Water System               18792\n",
      "STATEN ISLAND  Blocked Driveway            3465\n",
      "               HEAT/HOT WATER              2073\n",
      "               Illegal Parking             7574\n",
      "               Noise                       1926\n",
      "               Noise - Residential         6744\n",
      "               Noise - Street/Sidewalk      853\n",
      "               Street Condition           10560\n",
      "               Street Light Condition      6596\n",
      "               UNSANITARY CONDITION        1953\n",
      "               Water System                5349\n",
      "Unspecified    Blocked Driveway            1038\n",
      "               Illegal Parking             1294\n",
      "               Noise                          3\n",
      "               Noise - Residential          694\n",
      "               Noise - Street/Sidewalk      217\n",
      "               Street Condition              43\n",
      "               Street Light Condition      1396\n",
      "Name: complaint_type, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print result1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) Load '2010_population.csv' dataset into a dataframe as df2\n",
    "\n",
    "2) Sort \"Population\" column in descending order and limit first 10 rows. Save into a Pandas Series 'top_10_populous'\n",
    "\n",
    "3) Filter out df1 for rows with 'incident_zip' present in 'top_10_populous'\n",
    "\n",
    "4) Group df2 by incident zip, and for each zip count 'complaint_type' "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df2 = pd.read_csv('2010_census.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Zip Code ZCTA</th>\n",
       "      <th>2010 Census Population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1001</td>\n",
       "      <td>16769</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1002</td>\n",
       "      <td>29049</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1003</td>\n",
       "      <td>10372</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1005</td>\n",
       "      <td>5079</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1007</td>\n",
       "      <td>14649</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Zip Code ZCTA  2010 Census Population\n",
       "0           1001                   16769\n",
       "1           1002                   29049\n",
       "2           1003                   10372\n",
       "3           1005                    5079\n",
       "4           1007                   14649"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 33092 entries, 0 to 33091\n",
      "Data columns (total 2 columns):\n",
      "Zip Code ZCTA             33092 non-null int64\n",
      "2010 Census Population    33092 non-null int64\n",
      "dtypes: int64(2)\n",
      "memory usage: 517.1 KB\n"
     ]
    }
   ],
   "source": [
    "df2.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "top_10_populous = df2.sort_values(by=['2010 Census Population'], ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "result2 = df[df.incident_zip.isin(top_10_populous.index.tolist())][['incident_zip', 'complaint_type']].groupby(['incident_zip', 'complaint_type'])['complaint_type'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Series([], Name: complaint_type, dtype: int64)\n"
     ]
    }
   ],
   "source": [
    "print result2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Task 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
