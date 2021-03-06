/*
 * Presentational component
 */
import PropTypes from 'prop-types';
import React from 'react';
import _ from 'lodash';
import moment from 'moment-timezone';

import ReactTable from '../../app/components/ReactTable';
import formatNumeric from '../../app/utilities/formatNumeric';
import history from '../../app/History';
import ROUTES_CREDIT_REQUESTS from '../../app/routes/CreditRequests';
import ROUTES_CREDITS from '../../app/routes/Credits';

const CreditTransactionListTable = (props) => {
  const { items } = props;
  const translateTransactionType = (item) => {
    if (!item.transactionType) {
      return false;
    }

    const { transactionType } = item.transactionType;
    switch (transactionType.toLowerCase()) {
      case 'validation':
        return 'Credit Application';
      default:
        return transactionType;
    }
  };

  const columns = [{
    Header: '',
    headerClassName: 'header-group',
    columns: [{
      accessor: 'foreignKey',
      className: 'text-center',
      Header: 'Transaction ID',
      id: 'id',
      maxWidth: 150,
    }],
  }, {
    Header: '',
    headerClassName: 'header-group date',
    columns: [{
      accessor: (item) => (moment(item.transactionTimestamp).format('YYYY-MM-DD')),
      className: 'text-center date',
      Header: 'Date',
      headerClassName: 'date',
      id: 'date',
      maxWidth: 200,
    }],
  }, {
    Header: '',
    headerClassName: 'header-group transaction',
    columns: [{
      accessor: (item) => translateTransactionType(item),
      className: 'text-left transaction',
      Header: 'Transaction',
      headerClassName: 'text-left transaction',
      id: 'transaction',
    }],
  }, {
    Header: 'Credits',
    headerClassName: 'header-group credits-left',
    columns: [{
      accessor: (item) => (item.creditsA ? formatNumeric(item.creditsA, 2) : '-'),
      className: 'text-right credits-left',
      Header: 'A',
      Cell: (item) => (
        <span className={item.value < 0 ? 'text-danger' : ''}>{item.value}</span>
      ),
      headerClassName: 'credits-left',
      id: 'credit-class-a',
      maxWidth: 175,
    }, {
      accessor: (item) => (item.creditsB ? formatNumeric(item.creditsB, 2) : '-'),
      className: 'text-right',
      Cell: (item) => (
        <span className={item.value < 0 ? 'text-danger' : ''}>{item.value}</span>
      ),
      Header: 'B',
      id: 'credit-class-b',
      maxWidth: 175,
    }],
  }, {
    Header: 'Balance',
    headerClassName: 'header-group balance-left',
    columns: [{
      accessor: (item) => (item.displayTotalA ? _.round(item.displayTotalA, 2).toFixed(2) : '-'),
      className: 'text-right balance-left',
      Cell: (item) => (
        <span className={item.value < 0 ? 'text-danger' : ''}>{item.value}</span>
      ),
      Header: 'A',
      headerClassName: 'balance-left',
      id: 'credit-balance-a',
      maxWidth: 175,
    }, {
      accessor: (item) => (item.displayTotalB ? _.round(item.displayTotalB, 2).toFixed(2) : '-'),
      className: 'text-right',
      Cell: (item) => (
        <span className={item.value < 0 ? 'text-danger' : ''}>{item.value}</span>
      ),
      Header: 'B',
      id: 'credit-balance-b',
      maxWidth: 175,
    }],
  }];

  return (
    <ReactTable
      className="credit-transaction-list-table"
      columns={columns}
      data={items}
      defaultSorted={[{
        id: 'date',
        desc: true,
      }]}
      filterable={false}
      getTrProps={(state, row) => {
        if (row && row.original) {
          return {
            onClick: () => {
              if (!row.original.transactionType) {
                return false;
              }

              const item = row.original;

              const { transactionType } = item.transactionType;
              switch (transactionType.toLowerCase()) {
                case 'validation':
                  history.push(
                    ROUTES_CREDIT_REQUESTS.DETAILS.replace(/:id/g, item.foreignKey),
                    { href: ROUTES_CREDITS.LIST },
                  );
                  break;
                default:
              }

              return false;
            },
            className: 'clickable',
          };
        }

        return {};
      }}
    />
  );
};

CreditTransactionListTable.defaultProps = {};

CreditTransactionListTable.propTypes = {
  items: PropTypes.arrayOf(PropTypes.shape({})).isRequired,
};

export default CreditTransactionListTable;
