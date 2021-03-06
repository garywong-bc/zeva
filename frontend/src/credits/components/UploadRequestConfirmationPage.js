import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import PropTypes from 'prop-types';
import React from 'react';
import { Link } from 'react-router-dom';
import Button from '../../app/components/Button';
import history from '../../app/History';

import CustomPropTypes from '../../app/utilities/props';
import ROUTES_CREDIT_REQUESTS from '../../app/routes/CreditRequests';

const UploadRequestConfirmationPage = (props) => {
  const {
    user,
    submissionId,
  } = props;

  const actionbar = (
    <div className="row">
      <div className="col-sm-12">
        <div className="action-bar">
          <span className="left-content">
            <span className="left-content">
              <FontAwesomeIcon icon="check" />Submission Complete!
            </span>
          </span>
          <span className="right-content">
            <Button buttonType="back" locationRoute={ROUTES_CREDIT_REQUESTS.LIST} />
            <button
              className="button"
              onClick={() => {
                history.push(ROUTES_CREDIT_REQUESTS.DETAILS.replace(/:id/g, submissionId));
              }}
              type="button"
            >
              <FontAwesomeIcon icon="link" /> View Submission
            </button>
          </span>
        </div>
      </div>
    </div>
  );

  return (
    <div id="sales-submission-confirmation" className="page">

      <div className="row">
        <div className="col-sm-12">
          <h1>{user.organization.name} ZEV Sales Submission {submissionId}</h1>
        </div>
      </div>

      <div className="row">
        <div className="col-sm-12">
          <h2>Submission Complete</h2>
          <p>
            Your submission has been received and will now be reviewed
            by The Province of British Columbia.
          </p>
          <p>
            {'You can view the status of your submission from the '}
            <Link to={ROUTES_CREDIT_REQUESTS.LIST}>
              Sales
            </Link>
            {' table at any time.'}
          </p>
        </div>
      </div>

      {actionbar}
    </div>
  );
};

UploadRequestConfirmationPage.defaultProps = {};

UploadRequestConfirmationPage.propTypes = {
  submissionId: PropTypes.string.isRequired,
  user: CustomPropTypes.user.isRequired,
};

export default UploadRequestConfirmationPage;
