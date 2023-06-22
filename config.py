import logging


class Config:

    APP_NAME = "moodle-quiz-archive-worker"
    """Name of this app."""

    VERSION = "0.1.0"
    """Version of this app."""

    LOG_LEVEL = logging.INFO
    """Python Logger logging level"""

    QUEUE_SIZE = 8
    """Maximum number of requests that are queued before returning an error."""

    HISTORY_SIZE = 128
    """Maximum number of jobs to keep in the history before forgetting about them."""

    REQUEST_TIMEOUT_SEC = 1800
    """Number of seconds before execution of a single request is aborted."""

    MOODLE_WSFUNCTION_ARCHIVE = 'quiz_archiver_generate_attempt_report'
    """Name of the Moodle webservice function to call to trigger an quiz attempt export"""

    MOODLE_WSFUNCTION_PROESS_UPLOAD = 'quiz_archiver_process_uploaded_artifact'
    """Name of the Moodle webservice function to call after an artifact was uploaded successfully"""

    REPORT_BASE_VIEWPORT_WIDTH = 1240
    """Width of the viewport created for rendering quiz attempts in pixel"""