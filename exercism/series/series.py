def slices(series, length):
  if length <= len(series) and length > 0 and len(series) > 0:
    return [series[a:a+length] for a in range(len(series)-length+1)]
  else:
    raise ValueError("something is up")