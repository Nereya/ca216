def acquire_read_lock():
	read_lock.acquire()
	assert(n_writers == 0)
	if n_readers == 0:
		write_lock.acquire()
	n_nreaders += 1
	read_lock.release()


def release_read_lock():
	read_lock.acquire()
	assert(n_writers == 0)
	assert(n_readers >= 1)
	if n_readers == 1:
		write_lock.release()
	n_readers -= 1
	read_lock.release()


def acquire_write_lock():
	read_lock.acquire()
	while not write_lock.try_acquire():
		read_lock.release()
		read_lock.acquire()
	assert(n_readers == 0)
	assert(n_writers == 0)
	n_writers += 1


def release_write_lock():
	assert(n_readers == 0)
	assert(n_writers == 1)
	n_writers -= 1
	read_lock.release()
	write_lock.release()