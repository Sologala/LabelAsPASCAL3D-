import numpy as np
def project_3d(x3d, object):
    if 'viewpoint' in object:
        # project the 3D points
        viewpoint = object['viewpoint']
        a = viewpoint['azimuth'] * np.pi / 180
        e = viewpoint['elevation'] * np.pi / 180
        d = viewpoint['distance']
        f = viewpoint['focal']
        theta = viewpoint['theta'] * np.pi / 180
        principal = np.array([viewpoint['px'], viewpoint['py']])
        viewport = viewpoint['viewport']
    else:
        x = []
        return x

    if d == 0:
        x = []
        return x

    # camera center
    C = np.zeros(3)
    C[0] = d * np.cos(e) * np.sin(a)
    C[1] = -d * np.cos(e) * np.cos(a)
    C[2] = d * np.sin(e)

    # Rotate coordinate system by theta is equal to rotating the model by -theta.
    a = -a
    e = -(np.pi / 2 - e)

    # rotation matrix
    Rz = np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a),
                  np.cos(a), 0], [0, 0, 1]])  # rotate by a
    Rx = np.array([[1, 0, 0], [0, np.cos(e), -np.sin(e)],
                  [0, np.sin(e), np.cos(e)]])  # rotate by e
    R = np.dot(Rx, Rz)

    # perspective project matrix
    # however, we set the viewport to 3000, which makes the camera similar to
    # an affine-camera. Exploring a real perspective camera can be a future work.
    M = viewport
    P = np.dot(
        np.array([[M * f, 0, 0], [0, M * f, 0], [0, 0, -1]]), np.dot(R, -R * C))

    # project
    x = np.dot(P, np.vstack([x3d.T, np.ones(x3d.shape[0])]))
    x[0, :] = x[0, :] / x[2, :]
    x[1, :] = x[1, :] / x[2, :]
    x = x[:2, :].T

    # rotation matrix 2D
    R2d = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta), np.cos(theta)]])
    x = np.dot(R2d, x.T).T
    # x = x.T

    # transform to image coordinates
    x[:, 1] = -1 * x[:, 1]
    x = x + np.tile(principal, (x.shape[0], 1))

    return x
# END: abpxx6d04wxr
