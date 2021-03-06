import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import PropTypes from 'prop-types';
import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';

const FileDrop = (props) => {
  const { setFiles, maxFiles } = props;
  const [dropMessage, setDropMessage] = useState('');
  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length > maxFiles) {
      setDropMessage(`Please select only ${maxFiles} file${maxFiles !== 1 ? 's' : ''}.`);
    } else {
      setDropMessage('');
      setFiles(acceptedFiles);
    }
  }, []);

  const { getRootProps, getInputProps } = useDropzone({ onDrop });
  return (
    <div {...getRootProps()}>
      <input {...getInputProps()} />

      <div className="file-upload">
        <FontAwesomeIcon icon="upload" />
        <br />
        Drag and Drop files here or <br />
        <button className="link text-center" type="button">browse to select a file from your machine to upload.</button>
        {dropMessage && (
          <div id="danger-text">{dropMessage}</div>
        )}
      </div>
    </div>
  );
};

FileDrop.propTypes = {
  setFiles: PropTypes.func.isRequired,
  maxFiles: PropTypes.number.isRequired,
};

export default FileDrop;
